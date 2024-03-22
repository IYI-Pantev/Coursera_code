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
