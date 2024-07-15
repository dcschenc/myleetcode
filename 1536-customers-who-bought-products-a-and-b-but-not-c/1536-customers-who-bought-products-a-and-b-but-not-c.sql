# Write your MySQL query statement below
-- select customer_id, customer_name
-- from Customers 
-- where customer_id in (
    select customer_id, customer_name
    from Orders join Customers using(customer_id)
    group by customer_id 
    having sum(product_name='A') > 0 and sum(product_name='B') > 0 
    and sum(product_name='C') = 0
-- )