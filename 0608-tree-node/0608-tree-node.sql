# Write your MySQL query statement below
select id, 
       CASE
            WHEN p_id IS NULL THEN 'Root' 
            WHEN id in (SELECT p_id FROM Tree) THEN 'Inner'
            ELSE 'Leaf'
        END as type
FROM Tree;