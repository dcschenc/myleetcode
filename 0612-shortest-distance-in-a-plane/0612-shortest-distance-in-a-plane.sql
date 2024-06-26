# Write your MySQL query statement below
select min(round(sqrt(abs(p1.x - p2.x) * abs(p1.x - p2.x) + abs(p1.y - p2.y) * abs(p1.y - p2.y)), 2))
         as shortest 
-- from Point2D p1 join Point2D p2
from Point2D p1, Point2D p2
where p1.x != p2.x or p1.y != p2.y
