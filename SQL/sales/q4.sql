SELECT
    product_name,
    COUNT(*) AS purchase_count
FROM
    sales
JOIN
    menu ON sales.product_id = menu.product_id
GROUP BY
    product_name
ORDER BY
    purchase_count DESC
LIMIT 1;