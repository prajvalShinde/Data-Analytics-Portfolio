-- Total revenue
SELECT ROUND(SUM(s.quantity*b.price),2) AS total_revenue FROM sales s JOIN books b ON s.book_id=b.book_id;
-- Top five books by revenue
SELECT b.title, SUM(s.quantity) AS units, ROUND(SUM(s.quantity*b.price),2) AS revenue
FROM books b JOIN sales s ON b.book_id=s.book_id GROUP BY b.book_id,b.title ORDER BY revenue DESC LIMIT 5;
-- Genre revenue
SELECT b.genre, ROUND(SUM(s.quantity*b.price),2) AS revenue FROM books b JOIN sales s ON b.book_id=s.book_id GROUP BY b.genre ORDER BY revenue DESC;
-- Window ranking
SELECT title, genre, price, DENSE_RANK() OVER (PARTITION BY genre ORDER BY price DESC) AS price_rank FROM books;
-- Price bands
SELECT title, CASE WHEN price>=350 THEN 'Premium' WHEN price>=200 THEN 'Mid' ELSE 'Budget' END AS price_band FROM books;
