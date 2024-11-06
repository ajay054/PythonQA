WITH CustomerPoints AS (
    SELECT
        s.customer_id,
        s.order_date,
        menu.price,
        CASE
            WHEN s.order_date >= '2021-01-07' AND m.join_date IS NOT NULL THEN 2 * menu.price
            ELSE menu.price
        END AS points_earned
    FROM sales s
    LEFT JOIN menu ON s.product_id = menu.product_id
    LEFT JOIN members m ON s.customer_id = m.customer_id
    WHERE s.order_date BETWEEN '2021-01-01' AND '2021-01-31'
)
SELECT
    customer_id,
    SUM(points_earned) AS total_points
FROM CustomerPoints
GROUP BY customer_id;