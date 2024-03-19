-- create table unnique_id with default 1 and unique for id:
CREATE TABLE IF NOT EXISTS unique_id 
(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)

)
