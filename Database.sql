-- Task 1: View Table Schema
SELECT * FROM retail_purchases;

-- Task 2: Query Purchases in 'Electronics' Category (Secondary Index)
SELECT customer_id, customer_name, purchase_date, product_id, product_category, amount
FROM retail_purchases
WHERE product_category = 'Electronics'
ORDER BY amount DESC;

-- Task 3: Query Purchases by Date Range (Non-Clustered Index)
SELECT customer_id, customer_name, purchase_date, product_id, product_category, amount
FROM retail_purchases
WHERE purchase_date LIKE '9/%/2026'
ORDER BY purchase_date ASC;