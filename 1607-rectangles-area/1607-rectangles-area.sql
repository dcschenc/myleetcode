# Write your MySQL query statement below
select a.id as P1, b.id as P2, abs(a.x_value - b.x_value) * abs(a.y_value - b.y_value) as AREA
from Points a join Points b on a.id < b.id
where a.x_value <> b.x_value and a.y_value <> b.y_value
order by area desc, a.id , b.id 