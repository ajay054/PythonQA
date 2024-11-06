WITH PointsEarned AS (
    SELECT
        customer_id,
        SUM(price) AS total_spending,
        SUM(CASE WHEN product_name = 'sushi' THEN price * 2 ELSE price END) AS total_points
    FROM
        sales
    JOIN
        menu ON sales.product_id = menu.product_id
    GROUP BY
        customer_id
)
SELECT
    customer_id,
    total_spending,
    total_points
FROM
    PointsEarned;