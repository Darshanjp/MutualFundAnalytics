import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned files
nav_df = pd.read_csv("data/processed/nav_history_cleaned.csv")
trans_df = pd.read_csv("data/processed/investor_transactions_cleaned.csv")
perf_df = pd.read_csv("data/processed/scheme_performance_cleaned.csv")
fund_df = pd.read_csv("data/raw/01_fund_master.csv")

# Load into SQLite
fund_df.to_sql("dim_fund", engine, if_exists="replace", index=False)
nav_df.to_sql("fact_nav", engine, if_exists="replace", index=False)
trans_df.to_sql("fact_transactions", engine, if_exists="replace", index=False)
perf_df.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("Database Loaded Successfully!")