import math

def get_mock_demand_data():
    return [
        {'product': 'Tomatoes', 'location': 'Mumbai Urban', 'price': 50.0, 'quantity': 100, 'season': 'peak'},
        {'product': 'Tomatoes', 'location': 'Rural Punjab', 'price': 45.0, 'quantity': 150, 'season': 'peak'},
        {'product': 'Potatoes', 'location': 'Mumbai Urban', 'price': 30.0, 'quantity': 200, 'season': 'normal'},
        {'product': 'Potatoes', 'location': 'Rural Punjab', 'price': 25.0, 'quantity': 250, 'season': 'normal'},
        {'product': 'Onions', 'location': 'Surat City', 'price': 40.0, 'quantity': 120, 'season': 'low'},
        {'product': 'Carrots', 'location': 'Village Bihar', 'price': 35.0, 'quantity': 80, 'season': 'peak'},
    ]

def calculate_demand_elasticity(data):
    product_elasticity = {}
    
    for item in data:
        product = item['product']
        if product not in product_elasticity:
            product_elasticity[product] = []
        
        # Calculate demand score: quantity/price ratio
        demand_score = item['quantity'] / item['price']
        product_elasticity[product].append({
            'location': item['location'],
            'price': item['price'],
            'quantity': item['quantity'],
            'demand_score': demand_score,
            'season': item['season']
        })
    
    return product_elasticity

def predict_optimal_price(elasticity_data):
    predictions = []
    
    for product, locations in elasticity_data.items():
        avg_demand = sum(loc['demand_score'] for loc in locations) / len(locations)
        
        for loc in locations:
            current_price = loc['price']
            current_quantity = loc['quantity']
            demand_score = loc['demand_score']
            
            # Demand-based pricing factors
            demand_factor = demand_score / avg_demand
            season_factor = {'peak': 1.2, 'normal': 1.0, 'low': 0.8}[loc['season']]
            location_factor = 1.15 if 'urban' in loc['location'].lower() or 'city' in loc['location'].lower() else 0.95
            
            # Calculate optimal price
            optimal_price = current_price * demand_factor * season_factor * location_factor
            price_change = ((optimal_price - current_price) / current_price) * 100
            
            predictions.append({
                'product': product,
                'location': loc['location'],
                'current_price': current_price,
                'predicted_price': optimal_price,
                'current_quantity': current_quantity,
                'price_change': price_change,
                'demand_level': 'High' if demand_score > avg_demand else 'Low'
            })
    
    return predictions

def display_predictions(predictions):
    print("\n" + "="*130)
    print(f"{'Product':<12} {'Location':<18} {'Current $':<10} {'Predicted $':<12} {'Change %':<10} {'Demand':<8} {'Action':<15}")
    print("="*130)
    
    for pred in predictions:
        change = pred['price_change']
        if change > 10:
            action = "INCREASE PRICE"
        elif change < -10:
            action = "DECREASE PRICE"
        else:
            action = "MAINTAIN PRICE"
            
        print(f"{pred['product']:<12} {pred['location']:<18} ${pred['current_price']:<9.2f} "
              f"${pred['predicted_price']:<11.2f} {change:<9.1f}% {pred['demand_level']:<8} {action:<15}")
    
    print("="*130)
    print("\nDemand Prediction Factors:")
    print("• High demand locations -> Price increase recommended")
    print("• Peak season -> 20% markup, Low season -> 20% discount")
    print("• Urban areas -> 15% premium, Rural areas -> 5% discount")

if __name__ == "__main__":
    print("DEMAND-BASED PRICE PREDICTION SYSTEM")
    print("Analyzing market demand patterns...")
    
    data = get_mock_demand_data()
    elasticity = calculate_demand_elasticity(data)
    predictions = predict_optimal_price(elasticity)
    display_predictions(predictions)