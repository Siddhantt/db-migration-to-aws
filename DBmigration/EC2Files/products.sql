CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    price INT,
    category VARCHAR(100)
);

INSERT INTO products (name, price, category) VALUES ('Laptop', 65000, 'Electronics');
INSERT INTO products (name, price, category) VALUES ('Shoes', 2500, 'Footwear');
INSERT INTO products (name, price, category) VALUES ('Book', 450, 'Education');
