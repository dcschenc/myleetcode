# Write your MySQL query statement below
with t as (
    select account_id, sum(amount) as income, date_format(day, '%Y%m') as month
    from Transactions 
    where type = 'Creditor'
    group by account_id, month
)

select distinct(t1.account_id)
from t t1 join t t2 join Accounts a
where t1.account_id = t2.account_id and t1.account_id = a.account_id 
      and t2.month = t1.month + 1 and t1.income > max_income and t2.income > max_income

