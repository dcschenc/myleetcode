# Write your MySQL query statement below
select p.product_id, round(ifnull(sum(price * units)/sum(units), 0), 2) as average_price 
from Prices p 
left join UnitsSold s on s.product_id = p.product_id and s.purchase_date between start_date and end_date
group by p.product_id