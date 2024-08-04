# Write your MySQL query statement below
with t as(
    select employee_id, sum((ceiling(timestampdiff(second, in_time, out_time) / 60))) / 60 as t, needed_hours
    from Employees left join Logs using(employee_id)
    group by employee_id having t is null or t < needed_hours
)
select employee_id from t