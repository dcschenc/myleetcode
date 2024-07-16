# Write your MySQL query statement below
select left_operand, operator, right_operand, 
    case 
    when operator = '>' then if(v1.value > v2.value, 'true', 'false')
    when operator = '<' then if(v1.value < v2.value, 'true', 'false')
    when operator = '=' then if(v1.value = v2.value, 'true', 'false')
    end as value
from Expressions e 
join Variables v1 on e.left_operand = v1.name
join Variables v2 on e.right_operand = v2.name