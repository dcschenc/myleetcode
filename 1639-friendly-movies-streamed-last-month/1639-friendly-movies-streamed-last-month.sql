# Write your MySQL query statement below
select distinct title 
from TVProgram join Content using(content_id) 
    where year(program_date) = 2020 and month(program_date) = 6 
    and Kids_content = "Y" and content_type = 'Movies'