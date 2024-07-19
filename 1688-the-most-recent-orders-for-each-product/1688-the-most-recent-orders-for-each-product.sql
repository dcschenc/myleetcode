# Write your MySQL query statement below
select product_name, product_id, order_id, order_date from(
    select product_id, order_id, order_date,
            rank() over(partition by product_id order by order_date desc) as rnk
    from Orders join Products using(product_id)
) a 
join Products using(product_id) where rnk = 1 
order by product_name, product_id, order_id
