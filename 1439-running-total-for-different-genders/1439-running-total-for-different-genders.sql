# Write your MySQL query statement below
select gender, day, 
    sum(score_points) OVER (PARTITION BY gender ORDER BY gender, day) as total 
from Scores
group by gender, day
order by gender, day