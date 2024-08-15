# Write your MySQL query statement below
select user_id from Loans 
group by user_id having sum(loan_type = 'Mortgage') >= 1 and sum(loan_type = 'Refinance') >= 1
order by user_id