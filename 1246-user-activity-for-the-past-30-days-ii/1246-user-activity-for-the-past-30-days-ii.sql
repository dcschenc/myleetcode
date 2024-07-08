# Write your MySQL query statement below
select ifnull(round(sum(session) / count(*), 2), 0) as average_sessions_per_user 
from (
    select count(distinct session_id) as session, user_id from Activity
    where activity_date <='2019-07-27' and activity_date > '2019-06-27'
    group by user_id
) as a