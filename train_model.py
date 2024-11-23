import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import joblib

def train_model():
    # Load the prepared data
    df = pd.read_csv('student_data.csv')
    
    # Prepare features and target
    features = ['marks_1', 'marks_2', 'marks_3', 'marks_4', 'marks_5',
                'attendance_1', 'attendance_2', 'attendance_3', 'attendance_4', 'attendance_5', 'attendance_6']
    
    X = df[features]
    X['marks_trend'] = X['marks_5'] - X['marks_1']
    y = df['marks_6']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train a Random Forest Regressor
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test_scaled)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Mean Squared Error: {mse}")
    print(f"R-squared Score: {r2}")
    
    # Save the model and scaler
    joblib.dump(model, 'student_performance_model.joblib')
    joblib.dump(scaler, 'scaler.joblib')
    
    print("Model trained and saved successfully.")

if __name__ == "__main__":
    train_model()

