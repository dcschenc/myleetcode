# Write your MySQL query statement below
with t as (
    select *, rank() over(partition by customer_id order by order_date) as rnk
    from Delivery
)

-- select round(sum(order_date=customer_pref_delivery_date)*100/count(*), 2) as immediate_percentage
select round(avg(order_date=customer_pref_delivery_date) * 100, 2) as immediate_percentage
from t where rnk = 1
