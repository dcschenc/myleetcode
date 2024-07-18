# Write your MySQL query statement below
select customer_name, customer_id, order_id, order_date from(
    select name as customer_name, customer_id, order_id, order_date, 
        rank() over(partition by customer_id order by order_date desc) as rnk
    from Customers join Orders using(customer_id)
) a where rnk <= 3 
order by customer_name, customer_id, order_date desc
