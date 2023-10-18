-- show students with score greater than 9

SELECT score, `name`
FROM second_table
WHERE score >= '10'
ORDER BY score DESC;
