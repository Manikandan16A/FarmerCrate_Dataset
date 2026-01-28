# Location-Based Pricing System - Farmer Crate

## Project Overview
The Farmer Crate Location-Based Pricing System is an intelligent pricing solution designed to recommend optimal product prices based on geographical zones. Built with Python and PostgreSQL, this system addresses the challenge of fair pricing across diverse regional markets by considering factors such as demand patterns, transportation costs, and local economic conditions.

## System Architecture
The application connects to a Neon PostgreSQL cloud database containing three primary tables: farmers (storing farmer details and zones), products (containing product information and current prices), and orders (tracking customer purchases and quantities). Using the psycopg library for database connectivity, the system retrieves data through SQL JOIN operations that combine information across these tables to create comprehensive pricing insights.

## Pricing Algorithms

### Rule-Based Zone Pricing
The first approach implements a straightforward conditional logic system that classifies zones into three categories. Urban and city zones receive a 15% markup (multiplier 1.15) to account for higher demand, increased logistics costs, and premium market positioning. Rural and village zones receive a 10% discount (multiplier 0.90) reflecting lower operational costs and direct farm-to-market advantages. All other zones receive a standard 5% markup (multiplier 1.05). For example, tomatoes with a base price of $50 in Mumbai Urban would be calculated as $50 × 1.15 = $57.50.

### K-Means Clustering Algorithm
The advanced approach leverages machine learning to discover natural pricing patterns in the data. The algorithm extracts two features from each order: base price and quantity, creating coordinate pairs like [50, 100]. K-Means clustering then groups these data points into three clusters by iteratively assigning points to the nearest centroid and recalculating centroids until convergence. The resulting clusters represent low-demand (high volume, low price), medium-demand (balanced), and high-demand (low volume, high price) patterns. Each cluster receives an appropriate multiplier: 0.90x for low-demand, 1.05x for medium-demand, and 1.15x for high-demand zones. This data-driven approach automatically adapts to actual market behavior rather than relying on predefined rules.

## Implementation Process
The system follows a four-step workflow. First, it establishes a secure SSL connection to the PostgreSQL database using provided credentials. Second, it executes SQL queries to retrieve farmer names, zones, product names, base prices, and order quantities. Third, it applies the selected pricing algorithm to calculate recommended prices with appropriate multipliers. Finally, it generates formatted output displaying all relevant information including the calculation breakdown and reasoning behind each price recommendation.

## Output and Benefits
The system produces clear, tabular output showing farmer name, product name, zone, base price, multiplier applied, recommended price, and the calculation formula used. This transparency ensures stakeholders understand exactly how prices are determined. The business benefits include fair pricing that reflects regional market conditions, profit optimization in high-demand areas, competitive advantages through strategic discounts in price-sensitive zones, and scalability to accommodate new products and regions automatically. The K-Means approach particularly excels with large datasets by learning from actual patterns rather than requiring manual rule updates.

## Conclusion
This location-based pricing system provides Farmer Crate with a sophisticated yet practical tool for dynamic pricing decisions, balancing profitability with fairness across diverse geographical markets while maintaining complete transparency in pricing logic.
