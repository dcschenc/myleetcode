# Write your MySQL query statement below
with t as(
    select user_id,
        sum(case 
                when paid_by=user_id then -amount
                when paid_to=user_id then amount
                else 0 
                end
        ) as changes
    from Users join Transactions 
    group by user_id
)

select user_id, user_name, credit + changes as credit,
    if(credit + changes < 0, 'Yes', 'No') as credit_limit_breached 
from Users left join t using(user_id)
