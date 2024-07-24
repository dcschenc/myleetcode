# Write your MySQL query statement below
select p.player_id, player_name, count(*) grand_slams_count 
from (
    select Wimbledon as player_id from Championships
    union all
    select Fr_open as player_id from Championships
    union all
    select US_open as player_id from Championships
    union all
    select Au_open as player_id from Championships
) as c 
join Players p using(player_id)
group by player_id