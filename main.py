from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
import os

model_path = os.path.join('notebooks', 'best_model_engineered.pkl')
model = joblib.load(model_path)

# Set your threshold here
optimal_threshold = 0.1939

# Initialize FastAPI app
app = FastAPI(title="Breast Cancer Malignancy Prediction API", version="1.0")

# Define Input Schema
class PatientFeatures(BaseModel):
    features: list  # List of 39 features (full engineered feature vector)

# Define/predict endpoint
@app.post('/predict')
def predict_risk(input_data: PatientFeatures):
    features_array = np.array(input_data.features).reshape(1, -1)
    probability = model.predict_proba(features_array)[0][1]  # Probability for class 1 (Malignant)
    prediction = int(probability >= optimal_threshold)

    response = {
        "prediction": "Malignant" if prediction == 1 else "Benign",
        "probability_of_malignancy": round(float(probability), 4),
        "threshold_used": optimal_threshold
    }
    return response