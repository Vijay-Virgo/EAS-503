from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Load the saved model
try:
    model = joblib.load("weather_forecast_model.pkl")  # Replace with your model file
except Exception as e:
    raise RuntimeError(f"Error loading model: {e}")

# Initialize FastAPI app
app = FastAPI()

# Define the input schema
class WeatherInput(BaseModel):
    temperature: float
    humidity: float
    wind_speed: float
    pressure: float
    cloud_cover: float

# Define the prediction endpoint
@app.post("/predict")
def read_root():
    return {"message": "Hello, World!"}
def predict_weather(data: WeatherInput):
    try:
        # Prepare input for the model
        input_data = np.array([[data.temperature, data.humidity, data.wind_speed, data.pressure, data.cloud_cover]])
        # Make prediction
        prediction = model.predict(input_data)
        rain_status = "rain" if prediction[0] == 1 else "no rain"
        return {"rain_status": rain_status}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")
