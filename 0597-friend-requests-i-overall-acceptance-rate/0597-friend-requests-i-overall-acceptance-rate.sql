# Write your MySQL query statement below
SELECT ROUND(
    IFNULL(
        (SELECT COUNT(*) FROM (SELECT DISTINCT requester_id, accepter_id FROM RequestAccepted) as a)
            /
        (SELECT COUNT(*) FROM (SELECT DISTINCT sender_id, send_to_id FROM FriendRequest) as b),
    0)
, 2) AS accept_rate;

-- SELECT
--     ROUND(
--         IFNULL(
--         (SELECT COUNT(*) FROM (SELECT DISTINCT requester_id, accepter_id FROM RequestAccepted) as a)
--         /
--         (SELECT COUNT(*) FROM (SELECT DISTINCT sender_id, send_to_id FROM FriendRequest) as b),
--         0)
--     , 2) AS accept_rate;