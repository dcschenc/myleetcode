# Write your MySQL query statement below
with Co as(
    select *, row_number() over() as id 
    from Coordinates
)

select x, y from (
    select a.x as x, a.y as y
    from Co a, Co b 
    where a.x = b.y and a.y = b.x and a.x <= a.y and a.id != b.id

    union 

    select b.x as x, b.y as y
    from Co a, Co b 
    where a.x = b.y and a.y = b.x and b.x <= b.y and a.id != b.id
) t order by x, y