# Write your MySQL query statement below
select user_id, 
       ifnull(round(sum(action='confirmed') / count(*), 2), 0) as confirmation_rate
from Signups left join Confirmations using(user_id)
group by user_id