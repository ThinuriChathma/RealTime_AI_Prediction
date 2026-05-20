from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load('models/model.pkl')

@app.get('/')
def home():
    return {"message": "AI Prediction API Running"}

@app.post('/predict')
def predict(data: dict):

    input_data = pd.DataFrame([data])

    prediction = model.predict(input_data)

    return {"prediction": int(prediction[0])}