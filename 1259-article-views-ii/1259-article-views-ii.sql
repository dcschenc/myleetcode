# Write your MySQL query statement below
with t as(
    select viewer_id, count(distinct article_id) as cnt
    from Views 
    group by viewer_id, view_date
)

select distinct viewer_id as id from t 
where cnt > 1