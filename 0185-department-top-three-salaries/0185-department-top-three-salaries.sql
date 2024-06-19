# Write your MySQL query statement below
select d.name as Department, a.name as Employee, salary as Salary
From (select *, dense_rank() over(partition by departmentId order by salary desc) as rnk 
        from Employee) as a 
inner join Department as d on a.departmentId=d.id
where rnk <= 3