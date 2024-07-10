# Write your MySQL query statement below
with acc_weights as (
    select person_name, sum(weight) over (order by turn) as acc_weight from Queue 
)

select person_name 
from acc_weights   
where acc_weight <= 1000
order by acc_weight desc limit 1
