# Write your MySQL query statement below
select name, bonus from Employee as E left join Bonus as B on E.empId = B.empId where bonus < 1000 or bonus is Null