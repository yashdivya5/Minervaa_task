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


## Getting Started

### Prerequisites

- Python 3.9 or higher
- Docker (optional)
- Git

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/student-performance-predictor.git
   cd student-performance-predictor
2. Create a virtual environment (optional but recommended):

```shellscript
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```


3. Install dependencies:

```shellscript
pip install -r requirements.txt
```


4. Generate training data and train the model:

```shellscript
python data_generator.py
python train_model.py
```


5. Start the FastAPI server:

```shellscript
uvicorn main:app --reload
```




### Docker Setup

1. Build the Docker image:

```shellscript
docker build -t student-performance-predictor .
```


2. Run the container:

```shellscript
docker run -p 8000:8000 student-performance-predictor
```




## API Documentation

### Endpoints

#### GET /

Health check endpoint that returns a welcome message.

#### POST /predict

Predicts student performance based on historical data.

##### Request Body

```json
{
  "marks_1": 75.5,
  "marks_2": 78.2,
  "marks_3": 80.1,
  "marks_4": 82.3,
  "marks_5": 85.0,
  "attendance_1": 0.9,
  "attendance_2": 0.92,
  "attendance_3": 0.88,
  "attendance_4": 0.95,
  "attendance_5": 0.93,
  "attendance_6": 0.94
}
```

##### Response

```json
{
  "predicted_performance": 87.65,
  "learning_curve": "Improving"
}
```

## Testing the API

### Using Postman

1. Open Postman and create a new request
2. Set the request type to POST
3. Enter the URL: `http://localhost:8000/predict`
4. Go to the "Headers" tab and add:

1. Key: `Content-Type`
2. Value: `application/json`



5. Go to the "Body" tab:

1. Select "raw"
2. Choose "JSON" from the dropdown
3. Enter the sample request body provided above



6. Click "Send" to test the endpoint


### Using curl

```shellscript
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{
           "marks_1": 75.5,
           "marks_2": 78.2,
           "marks_3": 80.1,
           "marks_4": 82.3,
           "marks_5": 85.0,
           "attendance_1": 0.9,
           "attendance_2": 0.92,
           "attendance_3": 0.88,
           "attendance_4": 0.95,
           "attendance_5": 0.93,
           "attendance_6": 0.94
         }'
```

## Model Information

The prediction model uses a Random Forest Regressor with the following features:

- Historical marks from previous semesters
- Attendance records
- Derived features including performance trends


The model is trained on synthetic data generated to simulate realistic student performance patterns. In a production environment, this should be replaced with real historical student data.



