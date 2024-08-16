# Write your MySQL query statement below
select concat(t1.topping_name, ',', t2.topping_name, ',', t3.topping_name) as pizza,
        t1.cost + t2.cost + t3.cost as total_cost
from Toppings t1, Toppings t2, Toppings t3 
where t1.topping_name < t2.topping_name and t2.topping_name < t3.topping_name
order by total_cost desc, pizza