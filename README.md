# Student Performance Prediction Streamlit App

## Description
This Streamlit web application predicts a student's performance score based on several input features. Users can enter their study hours per week, attendance percentage, mental health score, sleep hours, and part-time job status. The app applies a pre-trained machine learning model to estimate the student's performance score out of 100.

## Features
- Interactive sliders for numerical inputs: study hours, attendance, mental health score, and sleep hours.
- Dropdown for categorical input: part-time job (Yes/No).
- Predict button to generate and display the performance score prediction.
- Output score constrained between 0 and 100.

## Technologies Used
- Python
- Streamlit
- NumPy
- Joblib

## Setup and Usage
1. Clone this repository.
2. Ensure you have Python installed.
3. Install the dependencies:
4. Place the trained model file `student_performance_best_model.pkl` in the project root directory.
5. Run the Streamlit app:
6. Use the sliders and dropdowns to provide student data, then click "Predict Performance" to see results.

## Model Details
The model predicts student performance scores based on factors related to study habits, attendance, mental health, sleep, and part-time work.

