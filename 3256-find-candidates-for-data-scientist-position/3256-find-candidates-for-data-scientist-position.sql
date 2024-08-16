# Write your MySQL query statement below
select candidate_id 
from Candidates 
group by candidate_id 
having sum(skill in ('Python', 'Tableau', 'PostgreSQL')) = 3
order by candidate_id