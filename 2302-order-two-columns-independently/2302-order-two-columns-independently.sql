# Write your MySQL query statement below
select a.first_col as first_col, b.second_col as second_col
from (select first_col, row_number() over() as r from Data order by first_col) as a 
join
    (select second_col, row_number() over() as r from Data order by second_col desc) as b
using(r)

