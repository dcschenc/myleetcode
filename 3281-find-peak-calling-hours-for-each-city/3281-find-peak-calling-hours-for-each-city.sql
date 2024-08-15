# Write your MySQL query statement below
with t as (
    select city, hour(call_time) as hour, count(*) as cnt
    from Calls
    group by city, hour
)
select city, hour as peak_calling_hour, cnt as number_of_calls 
from t as t1
where cnt >= (select max(cnt) from t where city = t1.city)
order by peak_calling_hour desc, city desc