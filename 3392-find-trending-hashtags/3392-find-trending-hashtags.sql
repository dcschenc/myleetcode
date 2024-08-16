# Write your MySQL query statement below
select concat('#', substring_index(substring_index(tweet, '#', -1), ' ', 1)) as hashtag, count(*) as hashtag_count
from Tweets 
where year(tweet_date) = 2024 and month(tweet_date) = 2
group by hashtag 
order by hashtag_count desc, hashtag desc
limit 3