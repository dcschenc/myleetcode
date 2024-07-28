# Write your MySQL query statement below
with p as(
    select 'Android' as platform
    union
    select 'IOS'
    union
    select 'Web'
),
e as(
    select 'Reading' as experiment_name
    union
    select 'Sports'
    union 
    select 'Programming'
),
pe as(
    select * from p, e
)

select platform, experiment_name, ifnull(count(experiment_id), 0) as num_experiments
from pe left join Experiments using(platform, experiment_name)
group by platform, experiment_name