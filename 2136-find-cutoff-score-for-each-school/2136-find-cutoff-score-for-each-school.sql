# Write your MySQL query statement below
-- select school_id, score from Schools sl join(
-- select score, sum(student_count) over(order by score desc) as students from Exam
-- ) sc on sl.capacity >= students
-- group by school_id

select school_id, ifnull(min(score), -1) as score
from Schools left join Exam e on capacity >= student_count 
group by school_id
order by school_id
