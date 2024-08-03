# Write your MySQL query statement below
with t as (
    select product_id, count(order_id) as cnt, year(purchase_date) as year
    from Orders
    group by product_id, year
)

select distinct(product_id)
from t t1 join t t2 using(product_id)
where t2.year = t1.year + 1 and t1.cnt >= 3 and t2.cnt >= 3