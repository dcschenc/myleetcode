# Write your MySQL query statement below
select sum(weekday(submit_date) in (5, 6)) as weekend_cnt, sum(weekday(submit_date) not in (5, 6)) as working_cnt
from Tasks