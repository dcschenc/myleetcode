# Write your MySQL query statement below
select name, 
       ifnull(sum(rest), 0) as rest, ifnull(sum(paid), 0) as paid, 
       ifnull(sum(canceled),0) as canceled, ifnull(sum(refunded), 0) as refunded
from Product left join Invoice using(product_id)
group by product_id
order by name