-- Prepares a sample database, table and row in order to setup replication
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'replica_user_pwd';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
