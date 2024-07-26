# Write your MySQL query statement below
# Write your MySQL query statement below
SELECT 
    employee_id,
    IF(employee_id % 2 = 1 AND name NOT REGEXP '^M', salary, 0) AS bonus 
FROM 
    employees 
ORDER BY 
    employee_id

-- select employee_id, salary as bonus from Employees where employee_id % 2 = 1 and name not like 'M%'
-- union
-- select employee_id, 0 as bonus from Employees where not (employee_id % 2 = 1 and name not like 'M%')
-- order by employee_id