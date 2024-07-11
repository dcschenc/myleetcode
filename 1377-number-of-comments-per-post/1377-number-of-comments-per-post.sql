# Write your MySQL query statement below
SELECT s1.sub_id AS post_id, COUNT(DISTINCT s2.sub_id) AS number_of_comments
FROM Submissions AS s1
LEFT JOIN Submissions As s2 ON s1.sub_id = s2.parent_id
WHERE s1.parent_id IS Null
GROUP BY s1.sub_id
