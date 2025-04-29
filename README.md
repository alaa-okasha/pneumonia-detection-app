# 🩺 Pneumonia Detection App

This is a full-stack web application for detecting pneumonia from chest X-ray images using a deep learning model.

---
## 📁 Project Structure

```markdown
pneumonia-detection-app/
├── AI/            # Download model here 
│   ├── main.py
│   ├── requirements.txt         
├── frontend/            # React app (Vite)
│   └── ...
├── README.md
```
---
## 🔗 Download the Model

Please download the trained model file from Google Drive:

👉 [Download Model](https://drive.google.com/file/d/1LxFji4dL__slKNgqRbhzvBl0eIV65hw2/view?usp=sharing)

Then, place the model file inside the AI folder.

---

## ⚙️ How to Run the FastAPI Server (Backend)

1. Navigate to the backend folder
   ```bash
   cd AI
   ```
2. Open the folder in your IDE (pycharm recommended)
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
4.Run the server
```bash
uvicorn main:app --reload
```
🔗 By default, the API runs on: http://127.0.0.1:8000

---
   


