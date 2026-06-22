import requests
import pandas as pd
import os

funds = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

os.makedirs("data/raw", exist_ok=True)

for fund_name, scheme_code in funds.items():

    print(f"\nDownloading {fund_name}...")

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data["data"])

    file_path = f"data/raw/{fund_name}.csv"

    df.to_csv(file_path, index=False)

    print("Saved:", file_path)
    print("Rows:", len(df))