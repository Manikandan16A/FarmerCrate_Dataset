import sqlite3

# Create and populate local database
conn = sqlite3.connect('farmer_crate.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''CREATE TABLE IF NOT EXISTS farmers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    farmer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    total_price REAL,
    FOREIGN KEY (farmer_id) REFERENCES farmers(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
)''')

# Insert sample data
farmers = [
    (1, 'Rajesh Kumar', 'Mumbai Urban'),
    (2, 'Priya Sharma', 'Rural Punjab'),
    (3, 'Amit Patel', 'Surat City'),
    (4, 'Sunita Devi', 'Village Bihar'),
    (5, 'Vikram Singh', 'Delhi NCR')
]

products = [
    (1, 'Tomatoes', 50.0),
    (2, 'Potatoes', 30.0),
    (3, 'Onions', 40.0),
    (4, 'Carrots', 35.0),
    (5, 'Cabbage', 25.0)
]

orders = [
    (1, 1, 1, 100, 5000),
    (2, 2, 2, 200, 6000),
    (3, 3, 3, 150, 6000),
    (4, 4, 4, 120, 4200),
    (5, 5, 5, 180, 4500)
]

cursor.executemany('INSERT OR REPLACE INTO farmers VALUES (?, ?, ?)', farmers)
cursor.executemany('INSERT OR REPLACE INTO products VALUES (?, ?, ?)', products)
cursor.executemany('INSERT OR REPLACE INTO orders VALUES (?, ?, ?, ?, ?)', orders)

conn.commit()
conn.close()

print("✓ Database created: farmer_crate.db")
print("✓ Tables created: farmers, products, orders")
print("✓ Sample data inserted")
