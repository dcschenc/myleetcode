# Write your MySQL query statement below
with t as (
    select account_id, 
            case 
                when income < 20000 then 'Low Salary'
                when income <= 50000 then 'Average Salary'
                else 'High Salary'
            end 
            as category
    from Accounts
)

select category, sum(case when account_id is Null then 0 else 1 end) as accounts_count
from (select 'Low Salary' as category union select 'Average Salary' union select 'High Salary') a 
left join t using(category)
group by category