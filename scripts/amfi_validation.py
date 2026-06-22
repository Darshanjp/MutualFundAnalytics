import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Get unique AMFI codes
master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

# Validation
missing_codes = master_codes - nav_codes
matched_codes = master_codes.intersection(nav_codes)

print("=" * 60)
print("AMFI CODE VALIDATION REPORT")
print("=" * 60)

print(f"Fund Master Codes : {len(master_codes)}")
print(f"NAV History Codes : {len(nav_codes)}")
print(f"Matched Codes     : {len(matched_codes)}")
print(f"Missing Codes     : {len(missing_codes)}")

if len(missing_codes) == 0:
    print("\n✅ All AMFI Codes Validated Successfully")
else:
    print("\n⚠ Missing AMFI Codes:")
    print(list(missing_codes)[:20])