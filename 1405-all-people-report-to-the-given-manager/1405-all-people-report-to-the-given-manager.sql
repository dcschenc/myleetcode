# Write your MySQL query statement below
-- https://github.com/doocs/leetcode/tree/main/solution/1200-1299/1270.All%20People%20Report%20to%20the%20Given%20Manager
select e1.employee_id 
from Employees e1 
    join Employees e2 on e1.manager_id = e2.employee_id
    join Employees e3 on e2.manager_id = e3.employee_id
where e1.employee_id != 1 and e3.manager_id = 1