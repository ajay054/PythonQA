WITH PreMemberTotals AS (
    SELECT
        s.customer_id,
        COUNT(*) AS total_items,
        SUM(price) AS total_amount_spent
    FROM
        sales s
    JOIN
        menu m ON s.product_id = m.product_id
    LEFT JOIN
        members mem ON s.customer_id = mem.customer_id
    WHERE
        mem.customer_id IS NULL
    GROUP BY
        s.customer_id
)
SELECT
    customer_id,
    total_items,
    total_amount_spent
FROM
    PreMemberTotals;