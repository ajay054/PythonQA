WITH RankedItems AS (
    SELECT
        customer_id,
        product_name,
        COUNT(*) AS item_count,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY COUNT(*) DESC) AS rn
    FROM
        sales
    JOIN
        menu ON sales.product_id = menu.product_id
    GROUP BY
        customer_id,
        product_name
)
SELECT
    customer_id,
    product_name
FROM
    RankedItems
WHERE
    rn = 1;