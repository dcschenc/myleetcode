# Write your MySQL query statement below
with t as(
    select team_id, team_name, case
        when host_goals > guest_goals then 3
        when host_goals = guest_goals then 1
        else 0
        end as score
    from Matches m join Teams t on m.host_team = t.team_id
    union all
    select team_id, team_name, case
        when guest_goals > host_goals then 3
        when guest_goals = host_goals then 1
        else 0
        end as score
    from Matches m join Teams t on m.guest_team = t.team_id
)

select team_id, tt.team_name, ifnull(sum(score), 0) as num_points
from Teams tt left join t using(team_id) 
group by team_id
order by num_points desc, team_id
