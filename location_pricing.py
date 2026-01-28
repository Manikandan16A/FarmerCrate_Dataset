import psycopg
from psycopg.rows import dict_row

# Database connection
DB_CONFIG = {
    "host": "ep-autumn-brook-ad2tvvqx-pooler.c-2.us-east-1.aws.neon.tech",
    "port": 5432,
    "dbname": "neondb",
    "user": "neondb_owner",
    "password": "npg_OqQHNLEk4w7B",
    "sslmode": "require"
}

def get_location_based_pricing():
    conn = psycopg.connect(**DB_CONFIG)
    cursor = conn.cursor(row_factory=dict_row)
    
    query = """
    SELECT 
        f.name AS farmer_name,
        f.zone AS farmer_location,
        p.name AS product_name,
        o.quantity,
        p.current_price AS base_price,
        o.total_price,
        CASE 
            WHEN f.zone ILIKE '%urban%' OR f.zone ILIKE '%city%' THEN p.current_price * 1.15
            WHEN f.zone ILIKE '%rural%' OR f.zone ILIKE '%village%' THEN p.current_price * 0.90
            ELSE p.current_price * 1.05
        END AS recommended_price
    FROM orders o
    JOIN products p ON o.product_id = p.product_id
    JOIN farmers f ON p.farmer_id = f.farmer_id
    ORDER BY f.zone, f.name;
    """
    
    cursor.execute(query)
    results = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return results

def display_results(results):
    print("\n" + "="*140)
    print(f"{'Farmer Name':<20} {'Product':<20} {'Zone':<20} {'Base Price':<12} {'Multiplier':<12} {'Recommended':<12} {'Calculation':<30}")
    print("="*140)
    
    for row in results:
        zone = row['farmer_location'].lower()
        
        if 'urban' in zone or 'city' in zone:
            multiplier = 1.15
            calc = f"${row['base_price']:.2f} × 1.15 = ${row['recommended_price']:.2f}"
        elif 'rural' in zone or 'village' in zone:
            multiplier = 0.90
            calc = f"${row['base_price']:.2f} × 0.90 = ${row['recommended_price']:.2f}"
        else:
            multiplier = 1.05
            calc = f"${row['base_price']:.2f} × 1.05 = ${row['recommended_price']:.2f}"
            
        print(f"{row['farmer_name']:<20} {row['product_name']:<20} {row['farmer_location']:<20} "
              f"${row['base_price']:<11.2f} {multiplier:<12.2f} ${row['recommended_price']:<11.2f} {calc:<30}")
    
    print("="*140)
    print("\nPricing Logic:")
    print("  • Urban/City zones:    Base Price × 1.15 (+15% markup for high demand areas)")
    print("  • Rural/Village zones: Base Price × 0.90 (-10% discount for low cost areas)")
    print("  • Other zones:         Base Price × 1.05 (+5% standard markup)")

if __name__ == "__main__":
    try:
        results = get_location_based_pricing()
        display_results(results)
    except Exception as e:
        print(f"Error: {e}")
