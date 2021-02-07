-- Full, base database creation for Monitor Data
-- Do this once only
create database monitor;

CREATE USER 'monowner'@'%' IDENTIFIED BY 'm0n0wn3r';
CREATE USER 'monowner'@'localhost' IDENTIFIED BY 'm0n0wn3r';
GRANT ALL PRIVILEGES ON monitor . * TO 'monowner'@'localhost';
GRANT ALL PRIVILEGES ON monitor . * TO 'monowner'@'%';
FLUSH PRIVILEGES;
-- End of once only
