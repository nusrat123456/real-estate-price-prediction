import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("../data/train.csv")
df.fillna(df.median(numeric_only=True), inplace=True)
encoder = LabelEncoder()

for col in df.select_dtypes(include="object").columns:
    df[col] = encoder.fit_transform(df[col].astype(str))

df.to_csv("../data/clean_train.csv", index=False)    