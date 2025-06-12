import streamlit as st
import requests
import json

# Streamlit UI
st.title("House Price Prediction")

# Fetch locations from Flask API
try:
    response = requests.get("http://localhost:5000/locations")
    locations = response.json()['locations']
except:
    st.error("Error connecting to the backend server. Please ensure the Flask server is running.")
    locations = []

# Input fields
location = st.selectbox("Location", locations)
total_sqft = st.number_input("Total Square Feet", min_value=300, max_value=10000, value=1000)
bath = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)
bhk = st.number_input("Number of BHK", min_value=1, max_value=10, value=2)

# Predict button
if st.button("Predict Price"):
    try:
        # Send request to Flask API
        payload = {
            'location': location,
            'total_sqft': total_sqft,
            'bath': bath,
            'bhk': bhk
        }
        response = requests.post("http://localhost:5000/predict", json=payload)
        
        if response.status_code == 200:
            prediction = response.json()['prediction']
            st.success(f"Predicted House Price: ₹{prediction} Lakhs")
        else:
            st.error(response.json()['error'])
    except Exception as e:
        st.error(f"Error: {str(e)}")