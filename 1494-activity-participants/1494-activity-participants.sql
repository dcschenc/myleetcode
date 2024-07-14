# Write your MySQL query statement below
select activity from(
    select activity,
        rank() over (order by count(id)) as rank_asc,
        rank() over (order by count(id) desc) as rank_desc
    from Friends
    group by activity
) a
where rank_asc != 1 and rank_desc != 1