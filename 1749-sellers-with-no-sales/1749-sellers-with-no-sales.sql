# Write your MySQL query statement below
SELECT seller_name
FROM
    Seller
    LEFT JOIN Orders USING (seller_id)
GROUP BY seller_id
HAVING IFNULL(SUM(YEAR(sale_date) = 2020), 0) = 0
ORDER BY 1;

-- select seller_name from Seller s where seller_id not in (
--     select distinct(seller_id) from Orders where year(sale_date) = 2020
-- ) order by seller_name