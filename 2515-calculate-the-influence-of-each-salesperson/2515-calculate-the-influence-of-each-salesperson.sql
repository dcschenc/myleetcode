# Write your MySQL query statement below
select s.salesperson_id, name, ifnull(sum(price), 0) as total
from Salesperson s 
left join Customer using(salesperson_id) 
left join Sales using(customer_id)
group by s.salesperson_id