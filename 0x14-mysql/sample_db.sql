-- Prepares a sample database, table and row in order to setup replication
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
GRANT ALL PRIVILEGES ON tyrell_corp.* TO 'holberton_user'@'localhost';
CREATE TABLE IF NOT EXISTS nexus6(id INT PRIMARY KEY, name VARCHAR(200) NOT NULL);
INSERT INTO tyrell_corp.nexus6(id, name) VALUES(1, 'Leon');
