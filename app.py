import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("model.pkl")

# Page configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# Application title
st.title("🎓 Student Performance Predictor")

st.write(
    "Predict a student's writing score using "
    "their Mathematics and Reading scores."
)

st.divider()

# User inputs
st.subheader("Enter Student Marks")

math_score = st.number_input(
    "Mathematics Score",
    min_value=0,
    max_value=100,
    value=70
)

reading_score = st.number_input(
    "Reading Score",
    min_value=0,
    max_value=100,
    value=70
)

# Prediction button
if st.button("Predict Writing Score"):

    input_data = pd.DataFrame(
        [[math_score, reading_score]],
        columns=["math score", "reading score"]
    )

    prediction = model.predict(input_data)

    predicted_score = round(float(prediction[0]), 2)

    predicted_score = max(0, min(100, predicted_score))

    st.success(f"Predicted Writing Score: {predicted_score}")

    st.info(
        "This prediction is generated using a trained "
        "Linear Regression Machine Learning model."
    )