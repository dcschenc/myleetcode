# Write your MySQL query statement below
with t as(
    select Country.name as country, duration
    from Person 
        join Calls on id = caller_id or id = callee_id
        join Country on country_code = substring(phone_number, 1, 3)
)

select country
from t
group by country having avg(duration) > (select avg(duration) from t)