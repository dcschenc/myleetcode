# Write your MySQL query statement below
with all_products as(
    select distinct(product_id) as product_id from Products
),
t as(
    select product_id, new_price, 
    rank() over(partition by product_id order by change_date desc) as rnk
    from Products where change_date <= '2019-08-16'
)
select product_id, ifnull(new_price, 10) as price 
from all_products left join (select * from t where rnk = 1) a using(product_id) 
