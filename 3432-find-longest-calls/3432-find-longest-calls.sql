# Write your MySQL query statement below
WITH
    T AS (
        SELECT first_name, type,
            DATE_FORMAT(SEC_TO_TIME(duration), "%H:%i:%s") AS duration_formatted,
            RANK() OVER (PARTITION BY type ORDER BY duration DESC) AS rk
        FROM Calls AS c1 JOIN Contacts AS c2 ON c1.contact_id = c2.id
        )
SELECT
    first_name, type, duration_formatted
FROM T
WHERE rk <= 3
ORDER BY 2, 3 DESC, 1 DESC;

-- (select first_name, type,  date_format(sec_to_time(duration), "%H:%i:%s") as duration_formatted 
-- from Calls cl join Contacts ct on cl.contact_id = ct.id
-- where type = 'incoming' order by duration desc, first_name desc limit 3)
--     union 
-- (select first_name, type, date_format(sec_to_time(duration), "%H:%i:%s") as duration_formatted 
-- from Calls cl join Contacts ct on cl.contact_id = ct.id
-- where type = 'outgoing' order by duration desc, first_name desc limit 3)