# %%
import streamlit as st 
import numpy as np
import joblib

# Load trained components
model = joblib.load(r"C:\Users\AKHILK\BIA\Capstone\AKHIL-K BREASK CANCER RISK PREDICTION\STREAMLIT APP\Random_Forest.joblib")
scaler = joblib.load(r"C:\Users\AKHILK\BIA\Capstone\AKHIL-K BREASK CANCER RISK PREDICTION\STREAMLIT APP\scaler.joblib")
label_encoder = joblib.load(r"C:\Users\AKHILK\BIA\Capstone\AKHIL-K BREASK CANCER RISK PREDICTION\STREAMLIT APP\label_encoders.joblib")

st.title("🩺 Breast Cancer Survival Prediction")

# Input fields
st.subheader("Enter Patient Details:")

age = st.number_input("Age at Diagnosis", min_value=0, max_value=120, value=50)
cancer_type_detailed = st.number_input("Cancer Type Detailed (as encoded number)", min_value=0, value=1)
cancer_type = st.selectbox("Cancer Type", options=["Breast Cancer", "Breast Sarcoma"])
surgery_type = st.selectbox("Type of Breast Surgery", options=["Mastectomy", "Breast Conserving"])
cellularity = st.selectbox("Cellularity", options=["High", "Moderate", "Low"])
cohort = st.number_input("Cohort", value=2005)
patient_id = st.number_input("Patient ID", value=1)
chemotherapy = st.selectbox("Received Chemotherapy?", options=["Yes", "No"])

# Manual mapping (must match training label encoding)
cancer_type_map = {"Breast Cancer": 0, "Breast Sarcoma": 1}
surgery_map = {"Mastectomy": 0, "Breast Conserving": 1}
cellularity_map = {"High": 0, "Moderate": 1, "Low": 2}
chemo_map = {"Yes": 1, "No": 0}

# Convert input to array
input_data = np.array([[
    age,
    cancer_type_detailed,
    cancer_type_map[cancer_type],
    surgery_map[surgery_type],
    cellularity_map[cellularity],
    cohort,
    patient_id,
    chemo_map[chemotherapy]
]])

# Scale input
scaled_input = scaler.transform(input_data)

# Predict
if st.button("Predict Survival Status"):
    prediction = model.predict(scaled_input)[0]
    status = "🔴 Did Not Survive"if prediction == 1 else "🟢 Survived" 
    st.success(f"Prediction: {status}")



