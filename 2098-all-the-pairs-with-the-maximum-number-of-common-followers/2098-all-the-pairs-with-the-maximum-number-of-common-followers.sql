# Write your MySQL query statement below
SELECT user1_id,user2_id FROM 
(
    SELECT a.user_id AS user1_id, b.user_id AS user2_id,
        RANK () OVER (ORDER BY COUNT(a.follower_id) DESC) AS 'rnk'
    FROM Relations a JOIN Relations b ON a.user_id < b.user_id AND a.follower_id = b.follower_id
    GROUP BY user1_id, user2_id
) a 
WHERE rnk = 1