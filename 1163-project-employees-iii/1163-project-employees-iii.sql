# Write your MySQL query statement below
select project_id, employee_id from(
    select project_id, employee_id, 
            rank() over (partition by project_id order by experience_years desc) as rnk
    from Project 
    join Employee using(employee_id) 
) a
where rnk = 1
