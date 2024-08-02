CREATE PROCEDURE getUserIDs(startDate DATE, endDate DATE, minAmount INT)
BEGIN
	# Write your MySQL query statement below.
	select distinct user_id from Purchases 
    where time_stamp between timestamp(startDate) and timestamp(endDate) 
    and amount >= minAmount
    order by user_id;
END