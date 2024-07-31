# Write your MySQL query statement below
select
    bus_id,
    count(passenger_id) - lag(count(passenger_id), 1, 0) over(order by b.arrival_time) 
    as passengers_cnt
from Buses b left join Passengers p on p.arrival_time <= b.arrival_time
group by bus_id
order by bus_id