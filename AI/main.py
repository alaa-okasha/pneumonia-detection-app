from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import tensorflow as tf
import cv2

app = FastAPI()

# السماح لاي فرونت اند يوصل للسيرفر
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# تحميل الموديل
model = tf.keras.models.load_model('model12.h5')

# تجهيز الصورة قبل التوقع
def preprocess_image(image_bytes):
    img_array = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np.frombuffer(img_array, np.uint8), cv2.IMREAD_COLOR)
    img = cv2.resize(img, (128, 128))
    img = img / 255.0
    img = img.reshape(-1, 128, 128, 3)   # لاحظ هنا 3 بدل 1

    return img

# Endpoint للتوقع
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    processed_img = preprocess_image(contents)
    prediction = model.predict(processed_img)[0][0]

    if prediction > 0.5:
        diagnosis = "Normal"
        confidence = prediction
    else:
        diagnosis = "PNEUMONIA"
        confidence = 1 - prediction

    return {
        "diagnosis": diagnosis,
        "confidence": round(float(confidence) * 100, 2)
    }

# للتجربة فقط
@app.get("/")
def home():
    return {"message": "API is running!"}
