# Write your MySQL query statement below
with t as(
    select followee, count(distinct follower) as num
    from Follow
    group by followee
)

select followee as follower, num from t 
where followee in (select follower from Follow)
order by follower