# Write your MySQL query statement below
select transaction_id from Transactions t join 
(
    select max(amount) as max_amount, day from Transactions 
    group by day
) as m 
on t.day = m.day and t.amount = m.max_amount
order by transaction_id