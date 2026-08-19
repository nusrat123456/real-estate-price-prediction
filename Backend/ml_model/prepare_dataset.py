import pandas as pd
from pathlib import Path

# Project root
ROOT = Path(__file__).resolve().parent.parent.parent

# Input and output paths
input_file = ROOT / "Data" / "train.csv"
output_file = ROOT / "Data" / "house_prices.csv"

# Read Kaggle dataset
df = pd.read_csv(input_file)

# Create required columns
new_df = pd.DataFrame({
    "area": df["GrLivArea"],
    "bedrooms": df["BedroomAbvGr"],
    "bathrooms": df["FullBath"],
    "location": df["Neighborhood"],
    "price": df["SalePrice"]
})

# Save new dataset
new_df.to_csv(output_file, index=False)

print("Dataset created successfully!")
print(f"Saved at: {output_file}")
print(new_df.head())