import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("💧 ML-Based Water Intake Predictor")

weight = st.number_input("Weight (kg)", 30.0, 150.0, 70.0)
age = st.number_input("Age", 10, 90, 25)

activity = st.selectbox(
    "Activity Level",
    ["Sedentary", "Moderate", "Active"]
)

climate = st.selectbox(
    "Climate",
    ["Cold", "Moderate", "Hot"]
)

activity_map = {"Sedentary": 1, "Moderate": 2, "Active": 3}
climate_map = {"Cold": 1, "Moderate": 2, "Hot": 3}

if st.button("Predict 💧"):
    features = np.array([[weight, age, activity_map[activity], climate_map[climate]]])
    prediction = model.predict(features)
    st.success(f"Recommended daily water intake: **{prediction[0]:.2f} liters**")
