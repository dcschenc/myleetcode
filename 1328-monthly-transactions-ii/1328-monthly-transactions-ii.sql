# Write your MySQL query statement below
WITH
    T AS (
        SELECT * FROM Transactions
        UNION
        SELECT id, country, 'chargeback', amount, c.trans_date
        FROM Transactions AS t JOIN Chargebacks AS c ON t.id = c.trans_id
    )

SELECT
    DATE_FORMAT(trans_date, '%Y-%m') AS month, country,
    SUM(state = 'approved') AS approved_count,
    SUM(IF(state = 'approved', amount, 0)) AS approved_amount,
    SUM(state = 'chargeback') AS chargeback_count,
    SUM(IF(state = 'chargeback', amount, 0)) AS chargeback_amount
FROM T
GROUP BY country, month
HAVING approved_amount OR chargeback_amount;


-- with charges as(
--     select country, state, date_format(c.trans_date, '%Y-%m') as month, 
--     count(*) as chargeback_count, sum(amount) as chargeback_amount
--     from Chargebacks c join Transactions t on t.id = c.trans_id
--     group by country, month
-- ),
-- trans as (
--     select id, country, state, date_format(trans_date, '%Y-%m') as month, count(*) as approved_count, sum(amount) as approved_amount
--     from Transactions where state = 'Approved'
--     group by country, month
-- )

-- select t.month, country, ifnull(approved_count, 0) as approved_count, ifnull(approved_amount, 0) as approved_amount,
--         ifnull(chargeback_count, 0) as chargeback_count, ifnull(chargeback_amount, 0) as chargeback_amount
-- from trans t right join charges using(country, month)
