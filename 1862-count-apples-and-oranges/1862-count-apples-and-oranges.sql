# Write your MySQL query statement below
select sum(b.apple_count) +  ifnull(sum(c.apple_count), 0) as apple_count, 
    sum(b.orange_count) + ifnull(sum(c.orange_count), 0) as orange_count
from Boxes b left join Chests c using(chest_id)

-- select sum(apple_count) as apple_count, sum(orange_count) as orange_count
-- from (
--     select c.apple_count as apple_count, c.orange_count as orange_count 
--     from Boxes join Chests c using(chest_id) 
--     union all
--     select apple_count, orange_count from Boxes
-- ) as a