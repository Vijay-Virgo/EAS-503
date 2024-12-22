import streamlit as st
import requests

# Define the FastAPI endpoint URL
API_URL = "http://localhost:8000/predict"  # Replace with your FastAPI endpoint

# Streamlit app UI
st.title("Real-Time Weather Forecast Classification")

st.write("Enter the weather data below to classify if it will rain or not.")

# Input fields for weather data
temperature = st.number_input("Temperature (°C)", value=25.0, step=0.1)
humidity = st.number_input("Humidity (%)", value=50.0, step=0.1)
wind_speed = st.number_input("Wind Speed (m/s)", value=5.0, step=0.1)
pressure = st.number_input("Pressure (hPa)", value=1013.0, step=0.1)
cloud_cover = st.number_input("Cloud Cover (%)", value=50.0, step=0.1)

# Submit button
if st.button("Classify"):
    # Prepare the input payload for the API
    payload = {
        "temperature": temperature,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "pressure": pressure,
        "cloud_cover": cloud_cover,
    }

    # Send a POST request to the FastAPI endpoint
    try:
        st.write(f"Connecting to API: {API_URL}")  # Debugging line
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            try:
                result = response.json()
                if "rain_status" in result:
                    st.success(f"Prediction: {result['rain_status']}")
                else:
                    st.error(f"Unexpected response structure: {result}")
            except ValueError:
                st.error("Invalid JSON response from the API.")
        else:
            st.error(f"API returned an error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to API: {e}")
