# Write your MySQL query statement below
select distinct user_id 
from Purchases p1 join Purchases p2 using(user_id)
where p1.purchase_id != p2.purchase_id and p1.purchase_date <= p2.purchase_date and datediff(p2.purchase_date, p1.purchase_date) <= 7
order by user_id