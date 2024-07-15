# Write your MySQL query statement below
select id, year, ifnull(npv, 0) as npv 
from Queries left join NPV using(id, year)
order by id, year