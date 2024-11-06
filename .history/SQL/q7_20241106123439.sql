WITH PreMemberPurchases AS (
    SELECT
        s.customer_id,
        m.product_name,
        ROW_NUMBER() OVER (PARTITION BY s.customer_id ORDER BY s.order_date DESC) AS rn
    FROM
        sales s
    JOIN
        menu m ON s.product_id = m.product_id
    JOIN
        members mem ON s.customer_id = mem.customer_id
)
SELECT
    customer_id,
    product_name
FROM
    PreMemberPurchases
WHERE
    rn = 1;