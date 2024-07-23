# Write your MySQL query statement below
select e2.employee_id as employee_id, e2.name as name, 
       count(e1.employee_id) as reports_count, round(avg(e1.age), 0) as average_age 
from Employees e2 join Employees e1 on e2.employee_id = e1.reports_to
group by e1.reports_to having reports_count >= 1
order by employee_id