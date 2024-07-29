# Write your MySQL query statement below
select candidate_id 
from Candidates join Rounds using(interview_id) 
where years_of_exp >= 2
group by candidate_id having sum(score) > 15