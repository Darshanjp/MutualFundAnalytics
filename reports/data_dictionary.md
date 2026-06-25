# Data Dictionary

## 01_fund_master.csv

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Unique AMFI scheme code |
| fund_house | Text | Mutual fund company |
| scheme_name | Text | Scheme name |
| category | Text | Fund category |
| sub_category | Text | Sub category |

## 02_nav_history.csv

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Scheme code |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

## 08_investor_transactions.csv

| Column | Type | Description |
|----------|----------|----------|
| investor_id | Text | Investor identifier |
| transaction_type | Text | SIP/Lumpsum/Redemption |
| amount_inr | Float | Transaction amount |
| kyc_status | Text | Investor KYC status |