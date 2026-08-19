import joblib
import pandas as pd
from pathlib import Path

# model path
MODEL_PATH = Path(__file__).parent / "model.pkl"

# load model once
model = joblib.load(MODEL_PATH)

def predict_price(area, bedrooms, bathrooms, location):
    data = pd.DataFrame([{
        "area": float(area),
        "bedrooms": int(bedrooms),
        "bathrooms": int(bathrooms),
        "location": location
    }])

    prediction = model.predict(data)[0]
    return round(float(prediction), 2)