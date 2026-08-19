import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

# Dataset
df = pd.read_csv("D:\\Real Estate Price Prediction\\real-estate-price-prediction\\Data\\house_prices.csv")

# Required columns
df = df[["area", "bedrooms", "bathrooms", "location", "price"]]

X = df.drop("price", axis=1)
y = df["price"]

# Numeric & Categorical
numeric = ["area", "bedrooms", "bathrooms"]
categorical = ["location"]

preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numeric),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical)
])

model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(
        n_estimators=200,
        random_state=42
    ))
])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))

joblib.dump(model, "model.pkl")

print("Model Saved Successfully!")