# Write your MySQL query statement below
with t as(
    select count(distinct item_id) as num_items, seller_id
    from Orders join Users using(seller_id) join Items using(item_id)
    where item_brand != favorite_brand
    group by seller_id
)

select seller_id, num_items
from t where num_items = (select max(num_items) from t)