import pandas as pd
import numpy as np

# Loading Dataset 
df = pd.read_csv("data/final_superstore_sales.csv")

#  Customer and Business Insights 
print("\n========================= Customer and Business Insights ============================")

# 1. Counting unique customers
unique_customers = df['customer_name'].nunique()
print("\nNumber of unique customers:", unique_customers)

# 2. Identifying repeated buyers
repeat_buyers = (
    df.groupby('customer_name')['order_id']
      .nunique()
      .reset_index()
      .rename(columns={'order_id': 'loyalty_score'})
)
print("\nTop 10 Repeat Buyers:")
print(repeat_buyers.sort_values(by='loyalty_score', ascending=False).head(10))

# 3. Top 5 customers who bring most revenue
top_5_revenue = (
    df.groupby('customer_name')
      .agg(total_revenue=('sales', 'sum'))
      .sort_values(by='total_revenue', ascending=False)
      .head(5)
      .round(2)
)
print("\nTop 5 Customers by Revenue:")
print(top_5_revenue)

# 4. Loyalty metric: number of orders per customer
print("\nLoyalty Metric (Orders per Customer):")
print(repeat_buyers.sort_values(by='loyalty_score', ascending=False).head())

total_sales = df['sales'].sum()
total_customers = unique_customers
total_orders = df['order_id'].nunique()

AOV = total_sales / total_orders                # Average Order Value
purchase_freq = total_orders / total_customers  # Purchase Frequency

# Assuming average lifespan = 1 year
CLV = AOV * purchase_freq * 1

print(f"\nApproximate CLV: {CLV:.2f}")
