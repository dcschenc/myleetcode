# Write your MySQL query statement below
-- SELECT player_id, device_id FROM Activity 
-- WHERE (player_id, event_date) IN 
-- (
--     SELECT player_id, MIN(event_date) FROM Activity GROUP BY player_id
-- )

WITH
    T AS (
        SELECT
            *,
            RANK() OVER (
                PARTITION BY player_id
                ORDER BY event_date
            ) AS rk
        FROM Activity
    )
    
SELECT player_id, device_id
FROM T
WHERE rk = 1;