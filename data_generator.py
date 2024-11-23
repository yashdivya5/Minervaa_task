import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
def generate_student_data(num_students=1000, num_semesters=6):
    np.random.seed(42)
    data = []
    for student_id in range(1, num_students + 1):
        base_performance = np.random.normal(70, 10)
        improvement_rate = np.random.normal(1, 0.5)
        attendance_rate = np.random.normal(0.9, 0.05) 
        for semester in range(1, num_semesters + 1):
            semester_performance = base_performance + improvement_rate * semester
            semester_performance = max(0, min(100, semester_performance))
            attendance = min(1, max(0, np.random.normal(attendance_rate, 0.05)))
            
            data.append({
                'student_id': student_id,
                'semester': semester,
                'marks': semester_performance,
                'attendance': attendance,
            })
    
    df = pd.DataFrame(data)
    return df

def prepare_data(df):
    # Pivot the data to have each semester as a column
    df_pivoted = df.pivot(index='student_id', columns='semester', values=['marks', 'attendance'])
    df_pivoted.columns = [f'{col[0]}_{col[1]}' for col in df_pivoted.columns]
    
    # Reset index to make student_id a column again
    df_pivoted.reset_index(inplace=True)
    
    return df_pivoted

if __name__ == "__main__":
    df = generate_student_data()
    df_prepared = prepare_data(df)
    
    # Save the prepared data
    df_prepared.to_csv('student_data.csv', index=False)
    
    print("Data generated and saved as 'student_data.csv' successfully.")

