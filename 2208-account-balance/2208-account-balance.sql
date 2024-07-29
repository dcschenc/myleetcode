# Write your MySQL query statement below
select account_id, day, 
sum( if(type='Deposit', amount, -amount)
    -- case 
    --     when type='Deposit' then amount
    --     else -amount
    --     end
    ) 
    over(partition by account_id order by day) 
as balance
from Transactions group by account_id, day