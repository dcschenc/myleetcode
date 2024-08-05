# Write your MySQL query statement below
select e1.symbol as metal, e2.symbol as nonmetal from 
(select symbol from Elements where type = 'Metal') as e1, 
(select symbol from Elements where type = 'Nonmetal') as e2