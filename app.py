import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("best_random_forest.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Function to make predictions
def predict_heart_disease(features):
    prediction = model.predict([features])
    return "Disease Detected" if prediction[0] == 1 else "No Disease"

# Streamlit UI
st.title("Heart Disease Prediction App")
st.write("Enter patient details below:")

# Input fields
age = st.number_input("Age", min_value=20, max_value=100, value=50)
sex = st.selectbox("Sex (0=Female, 1=Male)", [0, 1])
resting_bp = st.number_input("Resting Blood Pressure", min_value=80, max_value=200, value=120)
cholesterol = st.number_input("Cholesterol Level", min_value=100, max_value=400, value=200)
max_hr = st.number_input("Maximum Heart Rate", min_value=60, max_value=220, value=150)
oldpeak = st.number_input("Oldpeak (ST Depression)", min_value=0.0, max_value=6.0, value=1.0, step=0.1)
exercise_angina = st.selectbox("Exercise-Induced Angina (0=No, 1=Yes)", [0, 1])
st_slope = st.selectbox("ST Slope (0=Down, 1=Flat, 2=Up)", [0, 1, 2])
chest_pain_ata = st.selectbox("Chest Pain Type: Atypical Angina (0=No, 1=Yes)", [0, 1])
resting_ecg_st = st.selectbox("Resting ECG: ST-T Wave Abnormality (0=No, 1=Yes)", [0, 1])

# Button to make predictions
if st.button("Predict"):
    user_features = np.array([age, sex, resting_bp, cholesterol, max_hr, oldpeak, exercise_angina, st_slope, chest_pain_ata, resting_ecg_st])
    result = predict_heart_disease(user_features)
    st.success(f"Prediction: {result}")
