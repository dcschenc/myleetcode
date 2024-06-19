# Write your MySQL query statement below

select distinct(l1.num) as ConsecutiveNums
from Logs l1
     join logs l2 on l1.id = l2.id - 1 and l1.num = l2.num
     join logs l3 on l2.id = l3.id - 1 and l2.num = l3.num

-- with t as (
--     select *, lag(num) over() as previous, lead(num) over() as next 
--     from logs
-- )

-- select num as ConsecutiveNums
-- from t
-- where previous = num and next = num