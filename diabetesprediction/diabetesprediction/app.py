import streamlit as st
import requests

st.title("Diabetes Prediction and Recommendations")

# Input form
age = st.number_input('Age', min_value=0, max_value=120)
bmi = st.number_input('BMI', min_value=0.0, max_value=50.0)
HbA1c_level = st.number_input('HbA1c Level', min_value=0.0, max_value=20.0)
blood_glucose_level = st.number_input('Blood Glucose Level', min_value=0.0, max_value=300.0)
gender = st.selectbox('Gender', options=['Male', 'Female'])
gender_mapping = {'Male': 0, 'Female': 1}
gender_encoded = gender_mapping[gender]
smoking_history = st.selectbox('Smoking History', options=['Never', 'Former', 'Current'])

# Label Encoding
smoking_history_mapping = {'Never': 0, 'Former': 1, 'Current': 2}
smoking_history_encoded = smoking_history_mapping[smoking_history]





if st.button('Get Prediction'):
    features = [age, HbA1c_level, blood_glucose_level, smoking_history_encoded]
    response = requests.post('http://127.0.0.1:5000/predict_rf', json={'features': features})
    
    if response.status_code == 200:
        result = response.json()
        prediction = result['prediction']
        recommendations = result['recommendations']
        
        st.write(f"Prediction: {'Diabetes Diagnosed' if prediction == 1 else 'No Diabetes'}")
        
        st.subheader("Recommendations")
        for key, value in recommendations.items():
            st.write(f"{key}: {value}")
    else:
        st.write("Error in API request")
