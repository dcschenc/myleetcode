# Write your MySQL query statement below
select name as warehouse_name, sum(Width * Length * Height * units) as volume  
from Warehouse join Products p using(product_id)
group by name
