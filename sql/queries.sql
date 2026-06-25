-- 1 Top 5 Funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2 Average NAV
SELECT AVG(nav) AS avg_nav
FROM fact_nav;

-- 3 Monthly Average NAV
SELECT strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

-- 4 Transaction Count by State
SELECT state, COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5 Expense Ratio below 1%
SELECT amfi_code, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6 Average Transaction Amount
SELECT AVG(amount_inr)
FROM fact_transactions;

-- 7 SIP Transactions Count
SELECT COUNT(*)
FROM fact_transactions
WHERE transaction_type='SIP';

-- 8 Fund Count by Category
SELECT category, COUNT(*)
FROM dim_fund
GROUP BY category;

-- 9 Highest 1-Year Return
SELECT scheme_name, return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- 10 KYC Status Distribution
SELECT kyc_status, COUNT(*)
FROM fact_transactions
GROUP BY kyc_status;