# Write your MySQL query statement below
with t as(
    select age_bucket, sum(if(activity_type='send', time_spent, 0)) as send, 
        sum(if(activity_type='open', time_spent, 0)) as open
    from Activities join Age using(user_id)
    group by age_bucket
)

select  age_bucket, 
        round(send * 100 / (send + open), 2) as send_perc,
        round(open * 100 / (send + open), 2) as open_perc
from t
