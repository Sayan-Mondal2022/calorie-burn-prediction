import streamlit as st
import pandas as pd 
import joblib

# Load the saved model
model = joblib.load("model.pkl")

# App title
st.title("🏋️‍♂️ Calorie Burn Prediction App")

st.write("Enter your details below to predict calories burned:")

# User inputs
# 1️⃣ Row 1: Gender & Age
col1, col2 = st.columns(2)
with col1:
    gender = st.selectbox("Gender", ("Male", "Female"))
with col2:
    age = st.number_input("Age", min_value=1, max_value=100, value=25)

# 2️⃣ Row 2: Height & Weight
col3, col4 = st.columns(2)
with col3:
    height = st.number_input("Height (cm)", min_value=100, max_value=250, value=175)
with col4:
    weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)

# 3️⃣ Row 3: Duration & Heart Rate
col5, col6 = st.columns(2)
with col5:
    duration = st.number_input("Workout Duration (minutes)", min_value=1, max_value=300, value=30)
with col6:
    heart_rate = st.number_input("Heart Rate (bpm)", min_value=40, max_value=220, value=110)

# 4️⃣ Row 4: Body Temperature (alone)
body_temp = st.number_input("Body Temperature (°F)", min_value=36.0, max_value=110.0, value=98.6)

# Convert gender to numeric (assuming your model used 0 = Female, 1 = Male)
gender_val = 1 if gender == "Male" else 0

# Create input DataFrame
input_data = pd.DataFrame([{
    "Gender": gender_val,
    "Age": age,
    "Height": height,
    "Weight": weight,
    "Duration": duration,
    "Heart_Rate": heart_rate,
    "Body_Temp": body_temp
}])

# Predict when button is clicked
if st.button("Predict Calories Burned 🔥"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Calories Burned: **{prediction:.2f} kcal**")
