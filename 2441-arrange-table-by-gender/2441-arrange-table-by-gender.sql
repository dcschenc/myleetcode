# Write your MySQL query statement below
WITH
    t AS (
        SELECT
            *,
            RANK() OVER (
                PARTITION BY gender
                ORDER BY user_id
            ) AS rk1,
            CASE
                WHEN gender = 'female' THEN 0
                WHEN gender = 'other' THEN 1
                ELSE 2
            END AS rk2
        FROM Genders
    )
SELECT user_id, gender
FROM t
ORDER BY rk1, rk2;

-- select user_id, gender from(
--     select user_id, gender, rank() over(partition by gender order by user_id) as rnk from Genders
-- ) a 
-- order by rnk, gender

-- with females as(
--     select user_id, gender, rank() over(partition by gender order by user_id) as rnk from Genders where gender = 'female'
-- ),
-- males as(
--     select user_id, gender, rank() over(partition by gender order by user_id) as rnk from Genders where gender = 'male'
-- ),
-- others as(
--     select user_id, gender, rank() over(partition by gender order by user_id) as rnk from Genders where gender = 'other'
-- )

-- select user_id, gender from females 
-- union 
-- select user_id, gender from males 
-- union 
-- select user_id, gender from others 
-- order by rnk
