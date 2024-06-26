# Write your MySQL query statement below
select distinct(a.seat_id) from Cinema as a join Cinema as b 
        on abs(b.seat_id - a.seat_id) = 1 and a.free = 1 and b.free = 1
        order by a.seat_id