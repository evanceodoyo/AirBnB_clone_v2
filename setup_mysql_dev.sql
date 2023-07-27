-- script that prepares a MySQL server for the project. 
-- create a database named hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create user hbnb_dev
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant all privileges on the database hbnb_dev_db to user
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- grant SELECT privilege to hbnb_dev on db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
