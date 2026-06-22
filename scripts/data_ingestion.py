import os
import pandas as pd

print("=" * 60)
print("MUTUAL FUND DATA INGESTION")
print("=" * 60)

data_folder = "data/raw"

if not os.path.exists(data_folder):
    print("Raw data folder not found!")
else:
    files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

    print(f"\nCSV Files Found: {len(files)}")

    for file in files:

        print("\n" + "=" * 60)
        print("FILE:", file)
        print("=" * 60)

        path = os.path.join(data_folder, file)

        try:
            df = pd.read_csv(path)

            print("Shape:")
            print(df.shape)

            print("\nData Types:")
            print(df.dtypes)

            print("\nFirst 5 Rows:")
            print(df.head())

        except Exception as e:
            print("Error:", e)