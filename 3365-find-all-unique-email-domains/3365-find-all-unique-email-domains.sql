# Write your MySQL query statement below
select substring_index(email, '@', -1) as email_domain, count(id) as count
from Emails where email like '%.com'
group by email_domain
order by email_domain