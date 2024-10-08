# Write your MySQL query statement below
-- with pairs as(
--     select * from Friends 
--     union 
--     select user_id2, user_id1 from Friends 
-- )
-- select * from friends
-- where (user_id1, user_id2) not in (
--     select a.user_id1, b.user_id1 from pairs a join pairs b on a.user_id2 = b.user_id2
-- )
-- order by user_id1, user_id2

WITH
    T AS (
        SELECT user_id1, user_id2 FROM Friends
        UNION ALL
        SELECT user_id2, user_id1 FROM Friends
    )
SELECT user_id1, user_id2
FROM Friends
WHERE
    (user_id1, user_id2) NOT IN (
        SELECT t1.user_id1, t2.user_id1
        FROM
            T AS t1
            JOIN T AS t2 ON t1.user_id2 = t2.user_id2
    )
ORDER BY 1, 2;