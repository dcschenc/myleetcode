# Write your MySQL query statement below
with recursive ids as (
    select 1 as n  # base Query Data is fetched in first iteration 
    union 
    select n + 1 from ids # After first iteration the data is fetched from this query till the termination condition is met 
    where n < (select max(customer_id ) from customers) # This is Termination condition for iteration without this, query will run till infinte time so it is must and compulsory 
)
select n as ids 
from ids 
where n not in (select customer_id from customers)