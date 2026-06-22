import requests
import pandas as pd
import os

scheme_code = 125497

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)
data = response.json()

print("Fund Name:")
print(data["meta"]["scheme_name"])

df = pd.DataFrame(data["data"])

output_folder = "data/raw"
os.makedirs(output_folder, exist_ok=True)

output_file = os.path.join(
    output_folder,
    "HDFC_Top100_NAV.csv"
)

df.to_csv(output_file, index=False)

print("\nSaved Successfully!")
print("File:", output_file)
print("Rows:", len(df))