# Real-Time AI Prediction Platform with Automated MLOps Pipeline

## Project Overview

This project is a simplified production-style MLOps platform developed as part of an internship assignment.

The system performs real-time machine learning predictions using a trained AI model and exposes prediction functionality through a FastAPI REST API.

The project also demonstrates core MLOps concepts including:
- Model training
- Experiment tracking
- Automated retraining
- Monitoring
- CI/CD integration
- Docker support
- GitHub integration

---

# Features

- Real-time AI prediction API
- Machine learning model training pipeline
- FastAPI backend service
- Experiment tracking using MLflow
- Automated retraining script
- Monitoring and drift checking script
- Dockerized application structure
- CI/CD pipeline using GitHub Actions
- Modular project structure

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | REST API framework |
| Scikit-learn | Machine learning |
| Pandas | Data processing |
| MLflow | Experiment tracking |
| Docker | Containerization |
| GitHub Actions | CI/CD pipeline |
| Jupyter Notebook | Model development |

---

# Project Structure

```bash
RealTime_AI_Prediction/
│
├── app.py
├── Dockerfile
├── retrain.py
├── monitor.py
├── requirements.txt
├── training.ipynb
├── README.md
│
├── models/
│   └── model.pkl
│
├── data/
│
└── .github/
    └── workflows/
        └── ci.yml
```

---

# Dataset

Dataset used:
Telco Customer Churn Dataset

Dataset source:
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

---

# Machine Learning Workflow

1. Load dataset
2. Data preprocessing
3. Encode categorical features
4. Split training and testing data
5. Train Random Forest model
6. Evaluate accuracy
7. Save trained model
8. Serve predictions through FastAPI

---

# API Endpoints

## Home Endpoint

```http
GET /
```

Response:

```json
{
    "message": "AI Prediction API Running"
}
```

---

## Prediction Endpoint

```http
POST /predict
```

Example Request:

```json
{
  "gender": 1,
  "SeniorCitizen": 0,
  "Partner": 1,
  "Dependents": 0,
  "tenure": 12,
  "PhoneService": 1,
  "MultipleLines": 0,
  "InternetService": 1,
  "OnlineSecurity": 0,
  "OnlineBackup": 1,
  "DeviceProtection": 0,
  "TechSupport": 0,
  "StreamingTV": 1,
  "StreamingMovies": 1,
  "Contract": 0,
  "PaperlessBilling": 1,
  "PaymentMethod": 2,
  "MonthlyCharges": 70,
  "TotalCharges": 850
}
```

Example Response:

```json
{
    "prediction": 1
}
```

---

# How to Run the Project

## 1. Clone Repository

```bash
git clone <repository-url>
```

---

## 2. Create Environment

```bash
conda create -n mlops python=3.11
conda activate mlops
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run API

```bash
uvicorn app:app --reload
```

---

## 5. Open Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

# Experiment Tracking

MLflow is used to track:
- Model type
- Accuracy score
- Experiment runs

---

# CI/CD Pipeline

GitHub Actions workflow automatically:
- Checks repository code
- Installs dependencies
- Executes pipeline validation

Workflow file:

```text
.github/workflows/ci.yml
```

---

# Monitoring

The monitoring module simulates:
- Prediction monitoring
- Data drift checking
- Monitoring report generation

---

# Automated Retraining

The retraining module simulates:
- Loading updated datasets
- Retraining model
- Saving updated models

---

# Docker Support

Dockerfile is included for containerized deployment.

Build command:

```bash
docker build -t mlops-app .
```

Run command:

```bash
docker run -p 8000:8000 mlops-app
```

---
# Monitoring Dashboard

A lightweight Streamlit dashboard was implemented for:
- Model monitoring
- Accuracy tracking
- Drift monitoring
- Retraining status
- System health monitoring

Run dashboard:

```bash
streamlit run dashboard.py
```

# Future Improvements

- Cloud deployment
- Real-time streaming predictions
- Advanced monitoring dashboards
- Automated scheduled retraining
- Database integration
- Kubernetes deployment

---

# Author

Internship Project Submission

Developed by:
Thinuri Chathma