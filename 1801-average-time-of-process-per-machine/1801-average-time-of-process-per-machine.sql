# Write your MySQL query statement below
-- https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1661.Average%20Time%20of%20Process%20per%20Machine
SELECT
    machine_id,
    ROUND(
        AVG(
            CASE
                WHEN activity_type = 'start' THEN -timestamp
                ELSE timestamp
            END
        ) * 2,
        3
    ) AS processing_time
FROM Activity
GROUP BY 1;

-- select machine_id, round(sum(process_time) / count(machine_id), 3) as processing_time 
-- from
-- (
--     select machine_id, process_id, max(timestamp) - min(timestamp) as process_time
--     from Activity 
--     group by machine_id, process_id
-- ) as a 
-- group by machine_id