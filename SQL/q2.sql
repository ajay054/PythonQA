SELECT
    customer_id,
    COUNT(DISTINCT order_date) AS days_visited
FROM
    sales
GROUP BY
    customer_id;