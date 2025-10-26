import pandas as pd
import numpy as np

# Loading Dataset 
df = pd.read_csv("data/cleaned_superstore_sales.csv")

print("\n=== BASIC TOTALS ===")
print("Total Sales:", df['sales'].sum())
print("Total Profit:", df['profit'].sum())
print("Total Quantity:", df['quantity'].sum())

# Checking Negative Profits 
print("\nChecking for negative profit values:")
negative_profit_count = (df['profit'] < 0).sum()
print("Negative Profit Count:", negative_profit_count)

# Keeping negative profits and just keeping flag
df['loss_flag'] = df['profit'] < 0
 


print("\n=== SALES ANALYSIS ===")
print(df['sales'].agg(['mean', 'median', 'std', 'min', 'max']))

print("\n=== PROFIT ANALYSIS ===")
print(df['profit'].agg(['mean', 'median', 'std', 'min', 'max']))

# Profit Margin Calculation 
print("\nChecking if there are zero sales entries:")
zero_sales_count = (df['sales'] == 0).sum()
print("Zero Sales Count:", zero_sales_count)

df['profit_margin'] = np.where(df['sales'] != 0, df['profit'] / df['sales'], np.nan)

print("\nDataFrame with Profit Margin:")
print(df.head())

# Correlation Matrix 
print("\n=== CORRELATION MATRIX ===")
corr_matrix = df[['sales', 'profit', 'quantity', 'discount']].corr()
print(corr_matrix)



# Saving final dataset
df.to_csv("data/final_superstore_sales.csv", index=False)
print("\nFiles saved successfully!")
