# Student Performance Predictor API

A machine learning-based API that predicts student performance based on historical marks and attendance data. This project uses Python, FastAPI, and scikit-learn to create a predictive model that can be easily integrated into educational applications.

## Project Overview

This project implements a machine learning model to predict student performance and identify learning trends. The system uses historical academic data including:
- Previous semester marks
- Attendance records
- Performance trends

## Technical Stack

- Python 3.9+
- FastAPI
- scikit-learn
- pandas
- Docker
- Joblib

## Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/student-performance-predictor.git
   cd student-performance-predictor
2. **Create a virtual environment (optional but recommended):**
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **Install dependencies:**
   pip install -r requirements.txt
4. **Generate training data and train the model:**
   python data_generator.py
   python train_model.py
5. **Start the FastAPI server:**
   uvicorn main:app --reload
