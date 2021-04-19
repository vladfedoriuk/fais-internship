CREATE DATABASE IF NOT EXISTS praktyki ;
CREATE USER 'praktyki'@'localhost' IDENTIFIED BY 'pass4praktyki';
GRANT ALL PRIVILEGES ON * . * TO 'praktyki'@'localhost';