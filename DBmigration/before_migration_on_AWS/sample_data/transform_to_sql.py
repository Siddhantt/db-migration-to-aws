import json
import os

# Get current file directory
base = os.path.dirname(__file__)
input_file = os.path.join(base, "products.json")
output_file = os.path.join(base, "products.sql")

# Load data from JSON
with open(input_file, "r") as f:
    products = json.load(f)

print(f"📦 Loaded {len(products)} products from products.json")

# Write SQL output
with open(output_file, "w") as out:
    # Create table schema
    out.write("""CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    price INT,
    category VARCHAR(100)
);\n\n""")

    # Insert statements
    for product in products:
        name = product.get("name", "").replace("'", "''")
        price = product.get("price", 0)
        category = product.get("category", "").replace("'", "''")

        out.write(
            f"INSERT INTO products (name, price, category) VALUES ('{name}', {price}, '{category}');\n"
        )

print(f"✅ products.sql created at: {output_file}")

