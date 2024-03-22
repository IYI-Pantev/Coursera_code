-- @block
CREATE TABLE customers(customerName VARCHAR(100), phoneNumber INT);

-- @block
ALTER TABLE customers ADD(age INT, nationality VARCHAR(50));

-- @block
ALTER TABLE customers DROP COLUMN age;

-- @block
ALTER TABLE customers MODIFY nationality VARCHAR(100);

-- @block
INSERT INTO customers (customerName, phoneNumber, nationality
)
VALUES ("Roland Adkins", 35988723, "Ireland");

-- @block
ALTER TABLE customers MODIFY phoneNumber VARCHAR(20);

-- @block
UPDATE customers SET phoneNumber="+359887231564" WHERE customerName="Roland Adkins";

-- @block
ALTER TABLE customers ADD(date DATE);

-- @block
INSERT INTO customers (date) VALUES (CURRENT_DATE());

-- @block
UPDATE customers SET date= CURRENT_DATE() WHERE customerName="Roland Adkins";

-- @block
UPDATE customers SET customerName="James Brown", phoneNumber="+359888963170", nationality="USA" WHERE customerName IS NULL;

-- @block
SELECT * FROM customers;

-- @block
SELECT customerName FROM customers;

-- @block

SELECT * FROM customers;

-- creating database restaurant for practise 
-- database schema from er-d

-- @block
CREATE DATABASE restaurant;

-- @block 
USE restaurant;

-- @block
CREATE TABLE tbl (
    table_ID INT,
    location VARCHAR(255),
    PRIMARY KEY (table_ID)
);
-- @block
ALTER TABLE tbl
CHANGE COLUMN table_ID table_id INT;

-- @block
CREATE TABLE waiter( 

    waiter_id INT, 

    name VARCHAR(150), 

    contact_no VARCHAR(10), 

    shift VARCHAR(10), 

    PRIMARY KEY (waiter_id) 

); 

-- @block
