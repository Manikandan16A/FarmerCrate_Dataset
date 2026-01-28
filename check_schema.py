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

# Get table columns
for table in ['farmers', 'products', 'orders']:
    print(f"\n{table.upper()} table columns:")
    cursor.execute(f"""
        SELECT column_name, data_type 
        FROM information_schema.columns 
        WHERE table_name = '{table}'
        ORDER BY ordinal_position
    """)
    for row in cursor.fetchall():
        print(f"  - {row['column_name']}: {row['data_type']}")

cursor.close()
conn.close()
