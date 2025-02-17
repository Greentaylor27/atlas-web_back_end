-- Creating a table of unique users
CREATE TABLE users IF NOT EXISTS (
   id  INT IS NOT NULL PRIMARY KEY
   email VARCHAR(255) IS NOT NULL UNIQUE
   name VARCHAR(255)
)
