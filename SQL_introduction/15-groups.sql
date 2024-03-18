-- count score duplicates:
SELECT score, COUNT(score) as 'number' FROM second_table
GROUP BY score HAVING COUNT(score) > 1;
