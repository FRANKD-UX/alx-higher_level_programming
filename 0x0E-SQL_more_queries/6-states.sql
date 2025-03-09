-- Create the database hbtn_0d_usa if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the created database
USE hbtn_0d_usa;

-- Create the table states if it does not already exist
CREATE TABLE IF NOT EXISTS states (
	    id INT AUTO_INCREMENT PRIMARY KEY,  -- id is auto-generated, cannot be null, and is a primary key
	    name VARCHAR(256) NOT NULL          -- name cannot be null
	);

