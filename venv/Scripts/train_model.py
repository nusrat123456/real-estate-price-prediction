import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("../data/train.csv")

# Sirf required columns
df = df[[
    "GrLivArea",
    "BedroomAbvGr",
    "FullBath",
    "Neighborhood",
    "SalePrice"
]]

# Missing values
df.fillna("Unknown", inplace=True)

# Encode Neighborhood
encoder = LabelEncoder()
df["Neighborhood"] = encoder.fit_transform(df["Neighborhood"])

# Save encoder
os.makedirs("../Backend/ml_model", exist_ok=True)
joblib.dump(encoder, "../Backend/ml_model/location_encoder.pkl")

# Features
X = df.drop("SalePrice", axis=1)
y = df["SalePrice"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("R² Score:", round(r2_score(y_test, pred), 4))

joblib.dump(model, "../Backend/ml_model/house_model.pkl")

print("Model Saved Successfully.")