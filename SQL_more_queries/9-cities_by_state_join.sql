-- lists all cities in database:
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id = states.id ORDER BY cities.id;
