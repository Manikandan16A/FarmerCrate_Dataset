import sqlite3

def get_location_based_pricing():
    conn = sqlite3.connect('farmer_crate.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    query = """
    SELECT 
        f.name AS farmer_name,
        f.location AS farmer_location,
        p.name AS product_name,
        o.quantity,
        p.price AS base_price,
        o.total_price,
        CASE 
            WHEN f.location LIKE '%urban%' OR f.location LIKE '%city%' OR f.location LIKE '%City%' OR f.location LIKE '%Urban%' THEN p.price * 1.15
            WHEN f.location LIKE '%rural%' OR f.location LIKE '%village%' OR f.location LIKE '%Rural%' OR f.location LIKE '%Village%' THEN p.price * 0.90
            ELSE p.price * 1.05
        END AS recommended_price
    FROM orders o
    JOIN farmers f ON o.farmer_id = f.id
    JOIN products p ON o.product_id = p.id
    ORDER BY f.location, f.name
    """
    
    cursor.execute(query)
    results = cursor.fetchall()
    
    conn.close()
    return results

def display_results(results):
    print("\n" + "="*100)
    print(f"{'Farmer Name':<20} {'Product':<20} {'Location':<20} {'Base Price':<12} {'Recommended Price':<18}")
    print("="*100)
    
    for row in results:
        print(f"{row['farmer_name']:<20} {row['product_name']:<20} {row['farmer_location']:<20} "
              f"${row['base_price']:<11.2f} ${row['recommended_price']:<17.2f}")
    
    print("="*100)

if __name__ == "__main__":
    try:
        results = get_location_based_pricing()
        display_results(results)
    except Exception as e:
        print(f"Error: {e}")
        print("\nRun 'python setup_local_db.py' first to create the database")
