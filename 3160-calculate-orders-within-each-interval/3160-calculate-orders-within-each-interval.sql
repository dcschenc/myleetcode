# Write your MySQL query statement below
with recursive intervals as (
    select 1 as interval_no
    union all
    select interval_no + 1
    from intervals where interval_no < ceil((select max(minute) from Orders) /6)
) 

select interval_no, sum(order_count) as total_orders
from Orders join intervals on minute > (interval_no - 1) * 6 and minute <= interval_no * 6
group by interval_no
order by interval_no
