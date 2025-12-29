import streamlit as st

st.set_page_config(
    page_title="💧 Water Intake Calculator",
    page_icon="💧",
    layout="centered"
)

st.title("💧 Water Intake Calculator")

weight = st.number_input("Weight (kg)", min_value=1.0, value=70.0)
age = st.number_input("Age", min_value=1, value=25)

gender = st.selectbox("Gender", ["Male", "Female", "Other"])

activity = st.selectbox(
    "Activity Level",
    ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"]
)

climate = st.selectbox(
    "Climate",
    ["Cold", "Moderate", "Hot"]
)

if st.button("Calculate 💧"):
    # Base intake
    water_ml = weight * 35

    # Age adjustment
    if age < 18:
        water_ml *= 0.9
    elif age > 55:
        water_ml *= 0.95

    # Activity adjustment
    activity_multiplier = {
        "Sedentary": 1.0,
        "Lightly Active": 1.1,
        "Moderately Active": 1.25,
        "Very Active": 1.5
    }
    water_ml *= activity_multiplier[activity]

    # Climate adjustment
    climate_multiplier = {
        "Cold": 0.95,
        "Moderate": 1.0,
        "Hot": 1.2
    }
    water_ml *= climate_multiplier[climate]

    water_liters = round(water_ml / 1000, 2)

    st.success(f"💧 Your recommended daily water intake is **{water_liters} liters**")