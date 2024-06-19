# Write your MySQL query statement below
SELECT name AS 'Customers'
FROM Customers
LEFT JOIN Orders ON Customers.Id = Orders.CustomerId
WHERE Orders.CustomerId IS NULL

-- select name as Customers from Customers 
-- where id not in (select distinct(customerId) from Orders)