# Write your MySQL query statement below
WITH
    t AS (
        SELECT dep_id, COUNT(emp_id) AS cnt
        FROM Employees
        GROUP BY dep_id
    )
select emp_name as manager_name, dep_id 
from Employees join t using(dep_id) 
where position='Manager' and cnt = (select max(cnt) from t)
order by dep_id