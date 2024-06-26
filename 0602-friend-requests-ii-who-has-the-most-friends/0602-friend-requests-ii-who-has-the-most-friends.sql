# Write your MySQL query statement below
-- with t as(
--     select accepter_id as id, count(requester_id) as num
--     from RequestAccepted 
--     group by accepter_id 
-- )
-- select id, num from t where num = (select max(num) from t)

with all_ids as (
    select requester_id as id from RequestAccepted
    union all
    select accepter_id as id from RequestAccepted 
)
select id, count(id) as num
from all_ids
group by id
order by num desc
limit 1