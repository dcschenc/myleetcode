# Write your MySQL query statement below
with t as(
    select count(distinct r.post_id) / count(distinct a.post_id) as daily 
    from Actions a left join Removals r using(post_id)
    where action = 'report' and extra = 'spam'
    group by action_date
)
select round(avg(daily) * 100, 2) as average_daily_percent from t