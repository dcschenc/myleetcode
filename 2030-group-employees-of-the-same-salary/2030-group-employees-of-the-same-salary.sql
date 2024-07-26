# Write your MySQL query statement below
select employee_id, name, e.salary, team_id from Employees e join (
    select salary,row_number() over(order by salary) as team_id
    from Employees group by salary having(count(employee_id) >= 2) 
) as team
where e.salary = team.salary 
order by team_id, employee_id