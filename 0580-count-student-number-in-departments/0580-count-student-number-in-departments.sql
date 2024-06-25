# Write your MySQL query statement below
select dept_name, ifnull(count(student_id), 0) as student_number
from Department left join Student using(dept_id)
group by dept_id
order by student_number desc, dept_name