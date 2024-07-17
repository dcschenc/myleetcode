# Write your MySQL query statement below
select company_id, employee_id, employee_name, round(salary * (1 - tax), 0) as salary
from Salaries join (
    select company_id, 
        case
            when max(salary) < 1000 then 0
            when max(salary) <= 10000 then 0.24
            else 0.49
            end as tax
    from Salaries
    group by company_id
) as a using (company_id)