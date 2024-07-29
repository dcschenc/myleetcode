# Write your MySQL query statement below
SELECT
    m.member_id,
    name,
    CASE
        WHEN COUNT(v.visit_id) = 0 THEN 'Bronze'
        WHEN 100 * COUNT(charged_amount) / COUNT(v.visit_id) >= 80 THEN 'Diamond'
        WHEN 100 * COUNT(charged_amount) / COUNT(v.visit_id) >= 50 THEN 'Gold'
        ELSE 'Silver'
    END AS category
FROM
    Members AS m
    LEFT JOIN Visits AS v ON m.member_id = v.member_id
    LEFT JOIN Purchases AS p ON v.visit_id = p.visit_id
GROUP BY member_id;

-- with c as (
--     select member_id, 
--     count(charged_amount) * 100 / count(visit_id) as rate
--     from Visits left join Purchases using(visit_id)
--     group by member_id
-- )
-- select member_id, name, 
-- case
--         when rate >= 80 then 'Diamond'
--         when rate >= 50 then 'Gold'
--         when rate >= 0 then 'Silver'
--         else 'Bronze'
--     end as category
-- from Members 
-- left join c using(member_id)
-- order by member_id