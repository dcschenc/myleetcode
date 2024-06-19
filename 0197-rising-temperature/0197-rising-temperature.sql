# Write your MySQL query statement below
# select w1.id from Weather w1, Weather w2 where w1.id = (w2.id + 1) and w1.temperature > w2.temperature
select w1.id from Weather w1, Weather w2 
where datediff(w1.recordDate, w2.recordDate) = 1 and w1.temperature > w2.temperature