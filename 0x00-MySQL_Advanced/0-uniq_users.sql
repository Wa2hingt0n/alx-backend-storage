-- Creates a table 'users' with three columns, `id`, 'email', and 'name'
-- 'id', integer, never null, auto increment and primary key
-- 'email', string (255 characters), never null and unique
-- 'name', string (255 characters)

CREATE TABLE IF NOT EXISTS users (
id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
email VARCHAR(255) NOT NULL UNIQUE,
name VARCHAR(255));
