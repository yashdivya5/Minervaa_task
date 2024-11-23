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

```bash
# Clone the repository
git clone https://github.com/yourusername/student-performance-predictor.git
cd student-performance-predictor

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Generate training data and train the model
python data_generator.py
python train_model.py

# Start the FastAPI server
uvicorn main:app --reload

### Docker Setup

1. Build the Docker image:

```shell
docker build -t student-performance-predictor .  # [Docker Build Docs](https://docs.docker.com/engine/reference/commandline/build)

2. Run the container:
docker run -p 8000:8000 student-performance-predictor  # [Docker Run Docs](https://docs.docker.com/engine/reference/commandline/run)
