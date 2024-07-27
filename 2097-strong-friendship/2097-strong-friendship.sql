# Write your MySQL query statement below
with cte as (
    select *
    from friendship 
    union
    select user2_id, user1_id
    from friendship
)

select c1.user1_id, c1.user2_id, count(*) as common_friend
from cte c1
  join cte c2 on c1.user2_id = c2.user1_id and c1.user1_id<c1.user2_id
  join cte c3 on c2.user2_id = c3.user1_id and c1.user1_id = c3.user2_id
group by c1.user1_id, c1.user2_id
having count(*) >= 3


-- WITH Friends AS (
--     SELECT user1_id, user2_id FROM Friendship
--     UNION
--     SELECT user2_id, user1_id FROM Friendship
-- ),
-- CommonFriends AS (
--     SELECT 
--         F1.user1_id AS user1_id,
--         F2.user1_id AS user2_id,
--         COUNT(*) AS common_friend
--     FROM Friends F1
--     JOIN Friends F2 ON F1.user2_id = F2.user2_id
--     WHERE F1.user1_id < F2.user1_id
--     GROUP BY F1.user1_id, F2.user1_id
--     HAVING COUNT(*) >= 3
-- )
-- SELECT CF.user1_id, CF.user2_id, CF.common_friend
-- FROM CommonFriends CF
-- JOIN Friendship F ON CF.user1_id = F.user1_id AND CF.user2_id = F.user2_id
-- ORDER BY CF.user1_id, CF.user2_id;