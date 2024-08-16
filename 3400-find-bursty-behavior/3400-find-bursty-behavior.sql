# Write your MySQL query statement below
with a as(select * from Posts where post_date between '2024-02-01' and '2024-02-28'),
     b as(select user_id, count(post_id) / 4 as avg_weekly_posts from a group by user_id),
c as(
    select user_id, post_date, 
    count(post_id) over(partition by user_id order by post_date range between interval 6 day preceding and current row) as cnt7
    from a
),
d as(select user_id, max(cnt7) as max_7day_posts from c group by user_id),
e as(
    select * from d join b using(user_id) having(avg_weekly_posts * 2 <= max_7day_posts) order by user_id
)
select * from e

