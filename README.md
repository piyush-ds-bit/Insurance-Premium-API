# 🛡️ Insurance Premium Predictor API

A powerful and lightweight RESTful API built with **FastAPI** to predict **insurance premium categories** (High, Medium, Low) based on a user's profile.

This project includes:
- A trained Machine Learning model
- A clean API using FastAPI
- Dockerized environment for easy deployment

---

## 🎯 Project Motivation

As an aspiring **Data Scientist**, I wanted to solve a practical classification problem using ML — insurance premium prediction.  
This project allowed me to apply ML, deployment, and containerization skills while building something real-world and scalable.

---

## 🚀 Features

- ✅ Accepts user data and returns premium risk category
- ✅ Built with FastAPI (high-speed Python API framework)
- ✅ Trained ML model integrated behind the scenes
- ✅ Docker-ready for quick and reproducible deployments
- ✅ Includes Swagger UI for interactive testing

---

## 📥 Input Format (JSON)

``json
{
  "age": 28,
  "weight": 65,
  "height": 172,
  "income_lpa": 10,
  "smoker": false,
  "city": "Delhi",
  "occupation": "Engineer"
}
---

## 📤 Output Format
json
Copy
Edit
{
  
  "predicted_category":output,
  "confidence":round(confidence,4),
  "class_probabilities":class_prob
}
---

## 🧠 ML Model
Model Type: Classification

Algorithms tried: Logistic Regression, Random Forest

Preprocessing: Label Encoding, Standard Scaling

Data: 1000 entries (tiered cities, occupations, smoker status, etc.)

---

## 🛠️ Tech Stack
Python 3.10+

FastAPI – for building the API

Scikit-learn – for ML model training

Uvicorn – ASGI server

Docker – for containerization

Pydantic – for request validation

---

## ⚙️ Local Development Setup
Clone the Repository

bash
Copy
Edit
git clone https://github.com/your-username/insurance-api.git
cd insurance-api
Create a virtual environment & install dependencies

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

pip install -r requirements.txt
Run the API Locally

bash
Copy
Edit
uvicorn main:app --reload
Visit:
👉 http://127.0.0.1:8000/docs — for Swagger UI

---

## 🐳 Running with Docker
Build the Docker Image

bash
Copy
Edit
docker build -t insurance-api .
Run the Container

bash
Copy
Edit
docker run -d -p 8000:8000 insurance-api
Open in browser:
👉 http://localhost:8000/docs

Logs can be viewed with docker logs [container-id]

---

## 📬 Contact Me
Piyush Kumar Singh
🌐 piyushkrsingh.lovable.app
📧 piyushjuly04@gmail.com

---

## 🙏 Acknowledgements
FastAPI & Scikit-learn Docs

Docker documentation

The open-source ML and DevOps community

---

## ⭐ Star This Repo
If you found this project useful or inspiring, consider giving it a ⭐ and sharing it with your peers!

“Data-driven risk assessment made real — with FastAPI and ML.”
