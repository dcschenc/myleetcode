# Write your MySQL query statement below
select u.user_id, name, ifnull(sum(distance), 0) as `traveled distance`
from Users u left join Rides r using(user_id)
group by user_id
order by u.user_id 