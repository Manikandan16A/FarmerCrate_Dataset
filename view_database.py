import psycopg
from psycopg.rows import dict_row

DB_CONFIG = {
    "host": "ep-autumn-brook-ad2tvvqx-pooler.c-2.us-east-1.aws.neon.tech",
    "port": 5432,
    "dbname": "neondb",
    "user": "neondb_owner",
    "password": "npg_OqQHNLEk4w7B",
    "sslmode": "require"
}

conn = psycopg.connect(**DB_CONFIG)
cursor = conn.cursor(row_factory=dict_row)

# Retrieve Farmers
print("\n" + "="*80)
print("FARMERS TABLE")
print("="*80)
cursor.execute("SELECT * FROM farmers LIMIT 10")
for row in cursor.fetchall():
    print(row)

# Retrieve Products
print("\n" + "="*80)
print("PRODUCTS TABLE")
print("="*80)
cursor.execute("SELECT * FROM products LIMIT 10")
for row in cursor.fetchall():
    print(row)

# Retrieve Orders
print("\n" + "="*80)
print("ORDERS TABLE")
print("="*80)
cursor.execute("SELECT * FROM orders LIMIT 10")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
print("\n" + "="*80)
