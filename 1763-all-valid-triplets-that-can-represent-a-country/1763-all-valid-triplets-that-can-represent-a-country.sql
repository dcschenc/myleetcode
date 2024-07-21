# Write your MySQL query statement below
-- SELECT member_A, member_B, c.student_name AS member_C
-- FROM (
--     SELECT
--         a.student_name AS member_A,
--         a.student_id AS id_A,
--         b.student_name AS member_B,
--         b.student_id AS id_B
--     FROM SchoolA a CROSS JOIN SchoolB b
--     WHERE a.student_id != b.student_id AND
--           a.student_name != b.student_name
-- ) AS abQuery CROSS JOIN SchoolC c
-- WHERE abQuery.id_A != c.student_id AND
--       abQuery.member_A != c.student_name AND
--       abQuery.id_B != c.student_id AND
--       abQuery.member_B != c.student_name


SELECT
    a.student_name AS member_A,
    b.student_name AS member_B,
    c.student_name AS member_C
FROM
    SchoolA AS a,
    SchoolB AS b,
    SchoolC AS c
WHERE
    a.student_name != b.student_name
    AND a.student_name != c.student_name
    AND b.student_name != c.student_name
    AND a.student_id != b.student_id
    AND a.student_id != c.student_id
    AND b.student_id != c.student_id