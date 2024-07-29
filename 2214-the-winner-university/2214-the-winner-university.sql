# Write your MySQL query statement below
-- SELECT 
--   CASE 
--     WHEN NY.excellent_students > CA.excellent_students THEN 'New York University'
--     WHEN NY.excellent_students < CA.excellent_students THEN 'California University'
--     ELSE 'No Winner'
--   END AS winner
-- FROM 
--   (
--     SELECT COUNT(*) as excellent_students FROM NewYork WHERE score >= 90
--   ) NY, 
--   (
--     SELECT COUNT(*) as excellent_students FROM California WHERE score >= 90
--   ) CA;

select case
            when ny.cnt > ca.cnt then 'New York University'
            when ny.cnt < ca.cnt then 'California University'
            else 'No Winner'
        end as winner
from (
    (select count(*) as cnt from NewYork where score >= 90) as ny,    
    (select count(*) as cnt from California where score >= 90) as ca
)