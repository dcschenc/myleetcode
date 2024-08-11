# Write your MySQL query statement below
select flight_id, 
       least(count(passenger_id), capacity) as booked_cnt,
       greatest(count(passenger_id) - capacity, 0) as waitlist_cnt
from Flights left join Passengers Using(flight_id)
group by flight_id
order by flight_id

-- with t as(
-- select flight_id, count(passenger_id) as cnt
-- from Passengers group by flight_id
-- )

-- select flight_id, if(capacity > cnt, cnt, capacity) as booked_cnt, 
--         if(capacity > cnt, 0, cnt - capacity) as waitlist_cnt
-- from Flights join t using(flight_id)

-- union 

-- select flight_id, 0, 0 
-- from Flights where flight_id not in (select flight_id from t)

-- order by flight_id