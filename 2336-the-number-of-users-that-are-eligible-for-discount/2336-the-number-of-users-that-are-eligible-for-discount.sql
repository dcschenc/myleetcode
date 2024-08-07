CREATE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT) RETURNS INT
BEGIN
  RETURN (
      select count(distinct user_id) from Purchases 
      where amount >= minAmount and time_stamp between startDate and endDate
  );
END