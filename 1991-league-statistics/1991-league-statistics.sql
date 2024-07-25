# Write your MySQL query statement below
with t as(
    select team_id, team_name, home_team_goals as goal_for,
        away_team_goals as goal_against, case
        when home_team_goals > away_team_goals then 3
        when home_team_goals = away_team_goals then 1
        else 0
        end as score
    from Matches m join Teams t on m.home_team_id = t.team_id
    union all
    select team_id, team_name,away_team_goals as goal_for,
        home_team_goals as goal_against, case
        when away_team_goals > home_team_goals then 3
        when away_team_goals = home_team_goals then 1
        else 0
        end as score
    from Matches m join Teams t on m.away_team_id = t.team_id
)

select tt.team_name, count(*) as matches_played, sum(score) as points,
    sum(goal_for) as goal_for, sum(goal_against) as goal_against, 
    sum(goal_for) - sum(goal_against) as goal_diff
from Teams tt join t using(team_id) 
group by team_id
order by points desc, goal_diff desc, team_name
