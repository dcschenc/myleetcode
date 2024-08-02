# Write your MySQL query statement below
with t as (
    select distinct(driver_id) from Rides
)

select t.driver_id, count(passenger_id) as cnt 
from t 
left join Rides as r on t.driver_id = r.passenger_id
group by t.driver_id