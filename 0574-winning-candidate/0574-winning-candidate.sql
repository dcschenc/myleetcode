# Write your MySQL query statement below
with result as(
    select name, count(*) as cnt
    from Candidate c join Vote v on c.id = v.candidateId
    group by c.id  
)

select name from result where cnt = (select max(cnt) from result)