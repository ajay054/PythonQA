WITH RankedSales AS (
    SELECT
        customer_id,
        product_name,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS rn
    FROM
        sales
    JOIN
        menu ON sales.product_id = menu.product_id
)
SELECT
    customer_id,
    product_name
FROM
    RankedSales
WHERE
    rn = 1;