# Write your MySQL query statement below
select city_id, day, degree from (
    select *, rank() over(partition by city_id order by degree desc, day) as rnk
    from Weather
) a where rnk = 1 order by city_id