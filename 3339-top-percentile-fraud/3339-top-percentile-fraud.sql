# Write your MySQL query statement below
select policy_id, state, fraud_score from
(select *, percent_rank() over(partition by state order by fraud_score desc) as rnk from Fraud) a
where rnk <= 0.05
order by state, fraud_score desc, policy_id