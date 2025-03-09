-- Create the database hbtn_0d_usa if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the created database
USE hbtn_0d_usa;

-- Create the table cities if it does not already exist
CREATE TABLE IF NOT EXISTS cities (
	    id INT AUTO_INCREMENT PRIMARY KEY,           -- id is auto-generated, cannot be null, and is a primary key
	    state_id INT NOT NULL,                       -- state_id cannot be null and will be a foreign key
	    name VARCHAR(256) NOT NULL,                  -- name cannot be null
	    FOREIGN KEY (state_id) REFERENCES states(id) -- state_id is a foreign key referencing the id from the states table
	);

