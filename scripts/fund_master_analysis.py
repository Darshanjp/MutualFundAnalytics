import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("\nColumns:")
print(df.columns.tolist())

print("\nDataset Shape:")
print(df.shape)

for col in df.columns:
    print(f"\nUnique values in {col}:")
    print(df[col].nunique())
    print("\nUnique Fund Houses:")
print(df["fund_house"].unique())

print("\nCategories:")
print(df["category"].unique())

print("\nSub Categories:")
print(df["sub_category"].unique())

print("\nRisk Categories:")
print(df["risk_category"].unique())