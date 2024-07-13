# Write your MySQL query statement below
select product_name, sum(unit) as unit 
from Orders join Products using(product_id)
-- where year(order_date) = 2020 and month(order_date) = 2 
where date_format(order_date, '%Y%m') = '202002'
group by product_id 
having unit >= 100