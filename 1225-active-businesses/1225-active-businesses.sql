# Write your MySQL query statement below
SELECT business_id FROM 
(
    SELECT business_id, event_type, occurrences, 
            avg(occurrences) OVER (PARTITION BY event_type) AS avg 
    FROM Events
) t0 
WHERE occurrences > avg 
GROUP BY business_id 
HAVING COUNT(*) > 1