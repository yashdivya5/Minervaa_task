from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

app = FastAPI()

# Load the trained model and scaler
model = joblib.load('student_performance_model.joblib')
scaler = joblib.load('scaler.joblib')

class StudentData(BaseModel):
    marks_1: float
    marks_2: float
    marks_3: float
    marks_4: float
    marks_5: float
    attendance_1: float
    attendance_2: float
    attendance_3: float
    attendance_4: float
    attendance_5: float
    attendance_6: float

@app.post("/predict")
async def predict_performance(student: StudentData):
    try:
        # Prepare input data
        input_data = pd.DataFrame([student.dict()])
        
        # Calculate marks trend
        input_data['marks_trend'] = input_data['marks_5'] - input_data['marks_1']
        
        # Ensure the order of features matches what the model expects
        feature_order = ['marks_1', 'marks_2', 'marks_3', 'marks_4', 'marks_5',
                         'attendance_1', 'attendance_2', 'attendance_3', 'attendance_4', 'attendance_5', 'attendance_6',
                         'marks_trend']
        input_data = input_data[feature_order]
        
        # Scale input data
        input_scaled = scaler.transform(input_data)
        
        # Make prediction
        prediction = model.predict(input_scaled)[0]
        
        # Determine learning curve
        marks_trend = input_data['marks_trend'].values[0]
        if marks_trend > 5:
            learning_curve = "Improving"
        elif marks_trend < -5:
            learning_curve = "Declining"
        else:
            learning_curve = "Stable"
        
        return {
            "predicted_performance": round(prediction, 2),
            "learning_curve": learning_curve
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Student Performance Prediction API"}

