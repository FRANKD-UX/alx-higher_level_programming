-- Create the database hbtn_0d_2 if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user_0d_2 if it does not already exist, and set the password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on the database hbtn_0d_2 to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;

