import streamlit as st  # noqa: F401
import numpy as np      # noqa: F401
import joblib           # noqa: F401
import warnings
warnings.filterwarnings("ignore")

model = joblib.load("student_performance_best_model.pkl")

st.title("Student Performance Prediction")

st.write("Enter student details to predict their performance:")

study_hours = st.slider("Study Hours per Week", 0.0, 12.0, 2.0)
attendance = st.slider("Attendance Percentage", 0, 100, 75)
mental_health = st.slider("Mental Health Score (1-10)", 1, 10, 5)
sleep_hours = st.slider("Sleep Hours per Night", 0.0, 12.0, 6.0)
part_time_job = st.selectbox("Part-time Job", ["Yes", "No"])
part_time_job_encoded = 1 if part_time_job == "Yes" else 0

if st.button("Predict Performance"):
    input_data = np.array([study_hours, attendance, mental_health, sleep_hours, part_time_job_encoded]).reshape(1, -1)
    prediction = model.predict(input_data)[0]

    prediction = max(0, min(100, prediction))  # Ensure score is between 0 and 100
    st.success(f"Predicted Performance Score: {prediction:.2f}")