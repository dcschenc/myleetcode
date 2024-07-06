# Write your MySQL query statement below
select distinct p.product_id, p.product_name
from Sales s left join Product p using (product_id)
group by p.product_id
having min(sale_date) >= '2019-01-01' and max(sale_date) <= '2019-03-31'

-- select product_id, product_name from Product 
-- join Sales using (product_id) 
-- where sale_date between '2019-01-01' and '2019-03-31' and 
-- product_id not in (
--     select product_id from Sales where sale_date < '2019-01-01' or sale_date > '2019-03-31'
-- )