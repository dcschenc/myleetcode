# Write your MySQL query statement below
with t as(
    select question_id, ifnull(sum(action='answer') / sum(action='show'), 0) as rate
    from SurveyLog
    group by question_id
    order by rate desc, question_id
)

select question_id as survey_log from t limit 1