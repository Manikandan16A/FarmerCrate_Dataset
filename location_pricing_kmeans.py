import psycopg
from psycopg.rows import dict_row
from sklearn.cluster import KMeans
import numpy as np

DB_CONFIG = {
    "host": "ep-autumn-brook-ad2tvvqx-pooler.c-2.us-east-1.aws.neon.tech",
    "port": 5432,
    "dbname": "neondb",
    "user": "neondb_owner",
    "password": "npg_OqQHNLEk4w7B",
    "sslmode": "require"
}

def get_data():
    conn = psycopg.connect(**DB_CONFIG)
    cursor = conn.cursor(row_factory=dict_row)
    
    query = """
    SELECT 
        f.farmer_id,
        f.name AS farmer_name,
        f.zone AS farmer_zone,
        p.name AS product_name,
        p.current_price AS base_price,
        o.quantity,
        o.total_price
    FROM orders o
    JOIN products p ON o.product_id = p.product_id
    JOIN farmers f ON p.farmer_id = f.farmer_id
    """
    
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return results

def kmeans_pricing(data):
    # Extract features: base_price and quantity
    features = np.array([[row['base_price'], row['quantity']] for row in data])
    
    # Apply K-Means clustering (3 clusters: low, medium, high demand zones)
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(features)
    
    # Calculate cluster centers and assign pricing tiers
    centers = kmeans.cluster_centers_
    sorted_clusters = np.argsort(centers[:, 0])  # Sort by price
    
    pricing_multipliers = {
        sorted_clusters[0]: 0.90,  # Low-price cluster: -10%
        sorted_clusters[1]: 1.05,  # Medium-price cluster: +5%
        sorted_clusters[2]: 1.15   # High-price cluster: +15%
    }
    
    # Apply pricing
    results = []
    for i, row in enumerate(data):
        cluster = clusters[i]
        multiplier = pricing_multipliers[cluster]
        recommended_price = float(row['base_price']) * multiplier
        
        results.append({
            'farmer_name': row['farmer_name'],
            'product_name': row['product_name'],
            'farmer_zone': row['farmer_zone'],
            'base_price': float(row['base_price']),
            'recommended_price': recommended_price,
            'cluster': cluster,
            'tier': 'Low' if cluster == sorted_clusters[0] else 'Medium' if cluster == sorted_clusters[1] else 'High'
        })
    
    return results

def display_results(results):
    print("\n" + "="*130)
    print(f"{'Farmer':<18} {'Product':<18} {'Zone':<12} {'Base Price':<12} {'Multiplier':<12} {'Recommended':<12} {'Reason':<30}")
    print("="*130)
    
    for row in results:
        tier = row['tier']
        multiplier = row['recommended_price'] / row['base_price']
        
        if tier == 'Low':
            reason = "Low demand zone (-10%)" 
        elif tier == 'High':
            reason = "High demand zone (+15%)"
        else:
            reason = "Medium demand zone (+5%)"
            
        print(f"{row['farmer_name']:<18} {row['product_name']:<18} {row['farmer_zone']:<12} "
              f"${row['base_price']:<11.2f} {multiplier:<12.2f} ${row['recommended_price']:<11.2f} {reason:<30}")
    
    print("="*130)
    print(f"\nAlgorithm: K-Means Clustering (3 clusters)")
    print(f"\nCalculation Formula: Recommended Price = Base Price × Multiplier")
    print(f"  • Low Tier (Cluster 0):    Base Price × 0.90 = -10% discount")
    print(f"  • Medium Tier (Cluster 1): Base Price × 1.05 = +5% markup")
    print(f"  • High Tier (Cluster 2):   Base Price × 1.15 = +15% premium")
    print(f"\nExample: If Base Price = $50 and zone is High demand:")
    print(f"         Recommended Price = $50 × 1.15 = $57.50")

if __name__ == "__main__":
    try:
        data = get_data()
        if not data:
            print("No data found in database")
        else:
            results = kmeans_pricing(data)
            display_results(results)
    except Exception as e:
        print(f"Error: {e}")
