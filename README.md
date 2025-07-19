# 🧠 Recognition Label Detector

A Flask-based microservice that uses **Amazon Rekognition** to detect labels from uploaded images.  
Built with AWS, S3, Rekognition, and Flask. Ideal for real-world cloud ML pipelines.

---

## 🚀 Features

- Upload any image via API
- Detects objects, people, facial features, and apparel
- Uses **AWS Rekognition**
- Temporary storage in **Amazon S3**
- Deletes the file after analysis
- JSON API ready for frontend integration

---

## 📦 Tech Stack

- 🐍 Python (Flask)
- ☁️ AWS (S3, Rekognition)
- 🔒 Secure `.env` secrets
- 📬 RESTful API

---

## 📂 Folder Structure

```bash
recognition-label-detector/
│
├── backend/
│ ├── app.py # Flask API
│ ├── recognition_utils.py # S3 & Rekognition logic
│ ├── .env # AWS credentials/config
│ ├── requirements.txt # Python dependencies
│
└── .venv/ (optional, for local dev)
```
---

## ⚙️ Setup Instructions

### 1. 🧪 Clone the Repo

```bash
git clone https://github.com/thereevemenezes/recognition-label-detector.git
cd recognition-label-detector/backend
```
---
### 2. 🐍 Create & Activate Virtual Environment (Windows)
```bash
python -m venv venv
venv\Scripts\activate 
```
---
### 3. 📦 Install Requirements
```bash
pip install -r requirements.txt
```
---
### 4. 🔐 Configure AWS Credentials
```bash
# Create a .env file inside the backend/ folder:

AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=us-east-1
S3_BUCKET=your-s3-bucket-name
```
---

### 5.Run the Server
```bash
python app.py
```

## Test with Postman
- Method: POST
- URL: http://127.0.0.1:5000/upload
- Body: form-data
    - Key: image → Type: File → Upload any image
You’ll get a JSON response with labels detected by AWS Rekognition.
---

### Example Response

```bash
{
  "labels": [
    {
      "Name": "Person",
      "Confidence": 99.9
    },
    {
      "Name": "Smile",
      "Confidence": 98.5
    }
  ]
}
```
---

## 📌 Notes

Ensure your IAM user has permissions for:

- rekognition:DetectLabels

- s3:PutObject

- s3:GetObject

Do not commit your .env file.

## Future Works

- Add frontend drag & drop UI

- Show bounding boxes on faces

- Deploy using Docker or AWS EC2