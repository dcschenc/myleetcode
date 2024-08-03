# Write your MySQL query statement below
with dept as (
    select department_id, count(student_id) as cnt
    from Students 
    group by department_id
),
ranks as (
    select student_id, department_id, 
    rank() over(partition by department_id order by mark desc) as rnk
    from Students
)

select student_id, department_id, ifnull(round((rnk - 1) * 100 / (cnt - 1), 2), 0) as percentage
from ranks join dept using(department_id)