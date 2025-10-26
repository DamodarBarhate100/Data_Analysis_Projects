import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Loading Dataset 
df = pd.read_csv("data/final_superstore_sales.csv")
print(df.head())
#  Visualization using pandas 
print("\n=========================  Visualization  ============================")
pivot_table = pd.pivot_table(df,values=['sales','profit'],columns=['category'],index='region',aggfunc='sum')
print(pivot_table.head())

# Monthly sales trend line.
df['order_date'] = pd.to_datetime(df['order_date'],errors='coerce')
print("\n Monthly Sales:")
monthly_sales = df.resample(on='order_date', rule='ME').agg({'sales':'sum'})
print(monthly_sales.head())

plt.plot(monthly_sales,color='red',linestyle='solid',marker='o')
plt.xlabel('Months',fontweight='bold')
plt.ylabel('Sales',fontweight='bold')
plt.title('Monthly Sales',fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('reports/visuals/monthly_sales_plot.png')

# Bar chart of top categories.
top_categories = df.groupby(by='category').agg(total_sales=('sales','sum'))
print("\n Top Categories according to sales:")
print(top_categories)
categories = top_categories.index
sales_values = top_categories['total_sales']
x_pos = range(len(categories))
plt.figure(figsize=(10, 6))
plt.bar(x_pos, height=sales_values, width=0.4, align='center',color=['skyblue', 'lightcoral', 'lightgreen'])
plt.xticks(x_pos, categories, rotation=45, ha='right', fontweight='bold')
plt.xlabel('Category', fontweight='bold',fontsize=12)
plt.ylabel('Sales', fontweight='bold',fontsize=12)
plt.title('Total Sales by Category', fontweight='bold',fontsize=15)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('reports/visuals/categories_sales.png')

# Heatmap of region vs category profit.
region_cat = pd.pivot_table(df,values=['profit'],columns=['category'],index='region',aggfunc='sum')
print("\n Region Vs Category")
print(region_cat)

plt.figure(figsize=(9, 6))

sns.heatmap(
    region_cat,
    cmap="YlGnBu",       
    linewidths=.5,      
    cbar_kws={'label': 'Total Profit'} 
)

plt.title('Region vs. Category Profit Heatmap', fontweight='bold', fontsize=14)
plt.ylabel('Region', fontweight='bold')
plt.xlabel('Category', fontweight='bold')

plt.tight_layout()
plt.savefig('reports/visuals/heatmap_region_category.png')