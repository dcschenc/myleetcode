# Write your MySQL query statement below
with t as (
    select *, rank() over(partition by user_id order by activity_date) as rnk
    from Traffic where activity = 'login'
)
select activity_date as login_date, count(distinct user_id) as user_count
from t where rnk = 1 and datediff('2019-06-30', activity_date) <= 90
group by activity_date 