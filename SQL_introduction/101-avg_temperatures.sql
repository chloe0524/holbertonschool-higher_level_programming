-- displays average temps from dump file:
SELECT city, AVG(avg_temp) as average_temperature FROM temperatures GROUP BY city ORDER BY average_tempDESC;
