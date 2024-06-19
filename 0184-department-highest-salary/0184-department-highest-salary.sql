# Write your MySQL query statement below
select d.name as Department, a.name as Employee, Salary 
from (
    select *, rank() over(partition by departmentId order by salary desc) as rnk from Employee
) a 
join Department d on a.departmentId = d.id 
where rnk = 1