from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class FareEstimate(BaseModel):
    passenger_name: str
    distance_km: float
    is_rush_hour: bool

@app.post("/estimator")
def calculate_fare(fare: FareEstimate):
    # Base rate 1500 ugx
    base_rate = 1500

    # Km rate 1000 ugx per km
    distance_cost = fare.distance_km * 1000

    total_fare = distance_cost + base_rate

    # Rush hour 500 ugx
    if fare.is_rush_hour:
        total_fare = total_fare + 500

    return{
        "Passenger": fare.passenger_name,
        "Distance_km": f"{distance_cost:.2f}",
        "Rush_hour": fare.is_rush_hour,
        "Total": f"{total_fare:.2f}"
    }

@app.get("/estimator")
def get_estimator():
    return {
        "message": "Welcome to the fare estimator API",
        "info": "Use the POST method to calculate fare estimates"
    }