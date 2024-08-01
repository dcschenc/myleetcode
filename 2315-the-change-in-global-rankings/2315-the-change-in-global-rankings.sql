# Write your MySQL query statement below
select team_id, name, (convert(rnk_1, signed) - convert(rnk_2, signed)) as rank_diff from
(
    select *, rank() over(order by points desc, name) as rnk_1,
        rank() over(order by new_points desc, name) as rnk_2
    from (
        select *, points + ifnull(points_change, 0) as new_points
        from TeamPoints left join PointsChange using(team_id)
    ) a

) b
