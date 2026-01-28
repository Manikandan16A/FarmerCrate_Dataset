# Location-Based Pricing System for Farmer Crate

## Project Overview
The Farmer Crate Location-Based Pricing System dynamically recommends product prices based on geographical zones, enabling fair pricing that reflects regional demand, transportation costs, and market conditions.

---

## System Architecture

### Database Schema
- **Farmers Table**: farmer_id, name, zone, phone, email
- **Products Table**: product_id, name, current_price, quantity, farmer_id
- **Orders Table**: order_id, product_id, quantity, total_price, customer_id

### Technology Stack
- **Language**: Python 3.x
- **Database**: PostgreSQL (Neon Cloud)
- **Libraries**: psycopg (database connectivity), scikit-learn (ML algorithms), numpy

---

## Pricing Algorithms

### 1. Rule-Based Zone Pricing
**Algorithm**: Conditional logic based on zone classification

**Process**:
1. Extract farmer zone from database
2. Apply zone-specific multiplier:
   - Urban/City zones: Base Price × 1.15 (+15% markup)
   - Rural/Village zones: Base Price × 0.90 (-10% discount)
   - Other zones: Base Price × 1.05 (+5% standard markup)
3. Calculate: Recommended Price = Base Price × Multiplier

**Example**:
```
Product: Tomatoes
Base Price: $50.00
Zone: Mumbai Urban
Calculation: $50.00 × 1.15 = $57.50
Reason: High demand urban area with increased logistics costs
```

---

### 2. K-Means Clustering Algorithm
**Algorithm**: Machine learning-based dynamic pricing

**Process**:
1. **Data Collection**: Extract base_price and quantity from orders
2. **Feature Engineering**: Create 2D feature vectors [price, quantity]
3. **Clustering**: Apply K-Means (k=3) to group similar patterns
   - Initialize 3 random centroids
   - Assign each data point to nearest centroid
   - Recalculate centroids as cluster means
   - Repeat until convergence
4. **Cluster Classification**:
   - Cluster 0 (Low): Low price + high volume → 0.90x multiplier
   - Cluster 1 (Medium): Medium price + medium volume → 1.05x multiplier
   - Cluster 2 (High): High price + low volume → 1.15x multiplier
5. **Price Calculation**: Recommended Price = Base Price × Cluster Multiplier

**Example**:
```
Product: Onions
Base Price: $40.00
Features: [40, 150] (price, quantity)
Cluster Assignment: Cluster 1 (Medium demand)
Calculation: $40.00 × 1.05 = $42.00
Reason: Medium demand pattern identified by ML algorithm
```

---

## Implementation Workflow

### Step 1: Database Connection
```python
Connect to PostgreSQL database using credentials
Establish secure SSL connection to Neon cloud
```

### Step 2: Data Retrieval
```sql
JOIN farmers, products, and orders tables
Extract: farmer_name, zone, product_name, base_price, quantity
```

### Step 3: Price Calculation
```python
Apply selected algorithm (Rule-Based or K-Means)
Calculate recommended price with multiplier
```

### Step 4: Output Generation
```python
Display: Farmer, Product, Zone, Base Price, Multiplier, Recommended Price
Show calculation breakdown and reasoning
```

---

## Output Format

```
================================================================================
Farmer Name    Product      Zone          Base Price  Multiplier  Recommended  
================================================================================
Rajesh Kumar   Tomatoes     Mumbai Urban  $50.00      1.15        $57.50
Priya Sharma   Potatoes     Rural Punjab  $30.00      0.90        $27.00
Amit Patel     Onions       Surat City    $40.00      1.15        $46.00
================================================================================

Pricing Logic:
  • Urban/City zones:    +15% markup (high demand, logistics costs)
  • Rural/Village zones: -10% discount (direct from farm, low costs)
  • Other zones:         +5% standard markup
```

---

## Business Benefits

1. **Fair Pricing**: Reflects actual regional market conditions
2. **Profit Optimization**: Maximizes revenue in high-demand zones
3. **Competitive Advantage**: Offers discounts in price-sensitive rural areas
4. **Data-Driven**: K-Means algorithm learns from actual order patterns
5. **Scalability**: Automatically adapts to new zones and products

---

## Files Structure

```
Farmer crate/
├── location_pricing.py          # Rule-based pricing (simple)
├── location_pricing_kmeans.py   # ML-based pricing (advanced)
├── view_database.py             # Database inspection tool
├── check_schema.py              # Schema verification
├── requirements.txt             # Python dependencies
└── README.md                    # This documentation
```

---

## Usage Instructions

### Installation
```bash
pip install -r requirements.txt
```

### Run Rule-Based Pricing
```bash
python location_pricing.py
```

### Run K-Means Pricing
```bash
python location_pricing_kmeans.py
```

### View Database Contents
```bash
python view_database.py
```

---

## Algorithm Comparison

| Feature              | Rule-Based          | K-Means Clustering    |
|---------------------|---------------------|-----------------------|
| Complexity          | Simple              | Advanced              |
| Adaptability        | Fixed rules         | Learns from data      |
| Setup Time          | Immediate           | Requires training     |
| Accuracy            | Good                | Excellent             |
| Maintenance         | Manual updates      | Auto-adjusts          |
| Best For            | Small datasets      | Large datasets        |

---

## Future Enhancements

1. **Real-time Pricing**: Dynamic updates based on demand fluctuations
2. **Seasonal Factors**: Incorporate harvest seasons and weather data
3. **Competition Analysis**: Integrate competitor pricing data
4. **Customer Segmentation**: Personalized pricing for different customer types
5. **API Integration**: RESTful API for mobile app integration

---

## Contact & Support

**Project**: Farmer Crate Location-Based Pricing
**Database**: Neon PostgreSQL Cloud
**Version**: 1.0
**Last Updated**: 2024

---

*This system ensures transparent, fair, and profitable pricing for all stakeholders in the Farmer Crate ecosystem.*
