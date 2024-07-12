# Write your MySQL query statement below
SELECT l1.log_id as start_id, l2.log_id as end_id 
FROM Logs l1, Logs l2
WHERE l1.log_id <= l2.log_id AND l1.log_id - 1 not in (SELECT * FROM Logs)
    AND l2.log_id + 1 not in (SELECT * FROM Logs)
Group by l1.log_id