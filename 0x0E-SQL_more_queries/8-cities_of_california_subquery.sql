-- lists all cities of california that can be found in the database
-- where the states table contain only one record where name = california
SELECT id, name FROM cities WHERE state_id = (
  SELECT id
  FROM states
  WHERE name='California'
) ORDER BY cities.id ASC;
