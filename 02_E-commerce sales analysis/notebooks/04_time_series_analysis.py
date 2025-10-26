import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Loading Dataset 
df = pd.read_csv("data/final_superstore_sales.csv")

# Convert order_date to datetime
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

# Time Series Analysis 
print("\n========================= Time Series Analysis ============================")

# Resample by month - sales, profit, unique orders
resampled_df = df.resample(rule='ME', on='order_date').agg({
    'sales': 'sum',
    'profit': 'sum',
    'order_id': 'nunique'  #count unique orders
})
resampled_df.rename(columns={'order_id': 'total_orders'}, inplace=True)

# Handling missing values
resampled_df = resampled_df.asfreq('ME', fill_value=0)

resampled_df['Month'] = resampled_df.index.strftime('%B %Y')

print(resampled_df.head())

# Best & worst months
best_month_sales = resampled_df.nlargest(1, 'sales').index[0].strftime('%B %Y')
worst_month_sales = resampled_df.nsmallest(1, 'sales').index[0].strftime('%B %Y')

print("\nBest month for sales:", best_month_sales)
print("Worst month for sales:", worst_month_sales)


#  Seasonality Analysis 
df['month'] = df['order_date'].dt.month_name()
df['quarter'] = df['order_date'].dt.to_period('Q')

monthly_avg_sales = df.groupby('month')['sales'].mean().sort_values(ascending=False)
print("\nAverage Sales by Month:\n", monthly_avg_sales)

quarterly_avg_sales = df.groupby('quarter')['sales'].mean().sort_values(ascending=False)
print("\nAverage Sales by Quarter:\n", quarterly_avg_sales)
