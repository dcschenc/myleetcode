# Write your MySQL query statement below
with spends as(
    select *, row_number() over(partition by user_id order by transaction_date) as row_no
    from Transactions 
)
select user_id, spend as third_transaction_spend, transaction_date as third_transaction_date 
from spends a
where row_no = 3 and spend > (select max(spend) from spends where user_id = a.user_id and row_no <= 2)
order by user_id
