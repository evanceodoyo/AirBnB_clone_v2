-- script that prepares a MySQL (test) server for the project. 
-- create a database named hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create user hbnb_test
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant all privileges on the database hbnb_test_db to user
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- grant SELECT privilege to hbnb_test on db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
