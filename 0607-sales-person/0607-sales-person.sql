# Write your MySQL query statement below
select name from SalesPerson where sales_id not in 
    (select sales_id from orders left join company using(com_id) where name = 'RED')

-- select name from SalesPerson
-- where name not in (
--     select s.name from SalesPerson s, Orders o, Company c 
--     where o.sales_id = s.sales_id and o.com_id = c.com_id and c.name = 'RED' 
-- )