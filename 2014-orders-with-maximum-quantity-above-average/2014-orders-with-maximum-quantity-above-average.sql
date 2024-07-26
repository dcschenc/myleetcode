# Write your MySQL query statement below
with a as (
    select order_id, sum(quantity)/count(product_id) as avg_qty, max(quantity) as mx_qty
    from OrdersDetails
    group by order_id
)
select order_id from a 
where mx_qty > (select max(avg_qty) from a)
