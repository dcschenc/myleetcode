# Write your MySQL query statement below
WITH
    t AS (
        SELECT
            visited_on,
            SUM(amount) OVER (
                ORDER BY visited_on ROWS 6 PRECEDING
            ) AS amount,
            RANK() OVER (
                ORDER BY visited_on ROWS 6 PRECEDING
            ) AS rk
        FROM
            (
                SELECT visited_on, SUM(amount) AS amount
                FROM Customer GROUP BY visited_on
            ) AS tt
    )
    
SELECT visited_on, amount, ROUND(amount / 7, 2) AS average_amount
FROM t
WHERE rk > 6;

-- select a.visited_on, sum(b.amount) as amount, round(sum(b.amount)/7, 2) as average_amount
-- from (select distinct visited_on from customer) as a 
-- join customer as b on datediff(a.visited_on, b.visited_on) between 0 and 6
-- where a.visited_on >= (select min(visited_on) from customer) + 6
-- group by a.visited_on
-- order by a.visited_on