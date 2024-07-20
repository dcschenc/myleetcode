# Write your MySQL query statement below
select customer_id, count(*) as count_no_trans 
from Visits left join Transactions using(visit_id) 
where transaction_id is Null 
group by customer_id