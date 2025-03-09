-- Create the table unique_id if it does not already exist
CREATE TABLE IF NOT EXISTS unique_id (
	    id INT NOT NULL DEFAULT 1 UNIQUE,  -- id must be unique and have a default value of 1
	    name VARCHAR(256)
	);

