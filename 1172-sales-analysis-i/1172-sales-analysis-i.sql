# Write your MySQL query statement below
select seller_id from Sales s join Product p
on s.product_id = p.product_id group by seller_id 
having sum(price) >= all(
    select sum(price) from sales group by seller_id
)

-- SELECT seller_id
-- FROM Sales
-- GROUP BY seller_id
-- HAVING
--     SUM(price) >= ALL(
--         SELECT SUM(price)
--         FROM Sales
--         GROUP BY seller_id
--     );