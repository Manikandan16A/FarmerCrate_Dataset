# Demo version with mock data (works without database connection)

def get_mock_data():
    return [
        {"farmer_name": "Rajesh Kumar", "product_name": "Tomatoes", "farmer_location": "Mumbai Urban", "base_price": 50.0, "quantity": 100},
        {"farmer_name": "Priya Sharma", "product_name": "Potatoes", "farmer_location": "Rural Punjab", "base_price": 30.0, "quantity": 200},
        {"farmer_name": "Amit Patel", "product_name": "Onions", "farmer_location": "Surat City", "base_price": 40.0, "quantity": 150},
        {"farmer_name": "Sunita Devi", "product_name": "Carrots", "farmer_location": "Village Bihar", "base_price": 35.0, "quantity": 120},
        {"farmer_name": "Vikram Singh", "product_name": "Cabbage", "farmer_location": "Delhi NCR", "base_price": 25.0, "quantity": 180},
    ]

def calculate_recommended_price(location, base_price):
    location_lower = location.lower()
    if 'urban' in location_lower or 'city' in location_lower:
        return base_price * 1.15  # +15% for urban
    elif 'rural' in location_lower or 'village' in location_lower:
        return base_price * 0.90  # -10% for rural
    else:
        return base_price * 1.05  # +5% for others

def display_results(results):
    print("\n" + "="*100)
    print(f"{'Farmer Name':<20} {'Product':<20} {'Location':<20} {'Base Price':<12} {'Recommended Price':<18}")
    print("="*100)
    
    for row in results:
        recommended = calculate_recommended_price(row['farmer_location'], row['base_price'])
        print(f"{row['farmer_name']:<20} {row['product_name']:<20} {row['farmer_location']:<20} "
              f"${row['base_price']:<11.2f} ${recommended:<17.2f}")
    
    print("="*100)

if __name__ == "__main__":
    print("DEMO MODE - Using mock data")
    print("(Database connection unavailable)\n")
    results = get_mock_data()
    display_results(results)
