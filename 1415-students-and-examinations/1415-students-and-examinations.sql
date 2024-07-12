# Write your MySQL query statement below
-- https://github.com/doocs/leetcode/tree/main/solution/1200-1299/1280.Students%20and%20Examinations
SELECT student_id, student_name, subject_name, COUNT(e.student_id) AS attended_exams
FROM 
    Students
    JOIN Subjects
    LEFT JOIN Examinations AS e USING (student_id, subject_name)
GROUP BY student_id, subject_name
ORDER BY student_id, subject_name