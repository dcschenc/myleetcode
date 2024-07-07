# Write your MySQL query statement below
select book_id, name
from books left join Orders using(book_id)
where available_from < '2019-05-23'
group by book_id
having sum(if(dispatch_date >= '2018-06-23', quantity, 0)) < 10