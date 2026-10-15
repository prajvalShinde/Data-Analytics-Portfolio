-- Product with highest sales revenue
SELECT product, SUM(quantity*unit_price) AS revenue FROM sales GROUP BY product ORDER BY revenue DESC LIMIT 1;
-- Category with most revenue
SELECT category, SUM(quantity*unit_price) AS revenue FROM sales GROUP BY category ORDER BY revenue DESC LIMIT 1;
-- Total quantity sold
SELECT SUM(quantity) AS total_quantity FROM sales;
-- Top three products by sales
SELECT product, SUM(quantity*unit_price) AS revenue FROM sales GROUP BY product ORDER BY revenue DESC LIMIT 3;
-- Category-wise average transaction profit
SELECT category, ROUND(AVG(quantity*(unit_price-unit_cost)),2) AS avg_profit FROM sales GROUP BY category;
