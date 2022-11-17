-- script that prepares a MySQL server for the project

-- creates given database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- creates user with corresponding password (if it doesn't exist)
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- grants all privileges to hbnb_test on hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- grants select privilege on performance_schema to hbnb_test
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
