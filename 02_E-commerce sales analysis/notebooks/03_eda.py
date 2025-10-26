import pandas as pd
import numpy as np

# Loading Dataset 
df = pd.read_csv("data/final_superstore_sales.csv")
# print(df.head())

#  Exploratory Data Analysis 
print("\n========================= Exploratory Data Analysis ============================")

# Top 10 products by sales
top_10_product = (df.groupby(by=['product_id','product_name'])
                  .agg(top_10_product = ('sales','sum'))
                  .nlargest(10,columns='top_10_product'))
print("\n Top 10 products by sales:")
print(top_10_product)

# Top 10 customers by revenue.
top_10_customers = (df.groupby(by=['customer_name'])
                  .agg(top_10_customers = ('sales','sum'))
                  .nlargest(10,columns='top_10_customers'))
print("\n Top 10 customers by revenue:")
print(top_10_customers)

# Most profitable vs least profitable products
most_profitable =  (df.groupby(by=['product_id','product_name'])
                  .agg(most_profitable = ('profit','sum'))
                  .nlargest(10,columns=['most_profitable']))

print("\n Most profitable products:")
print(most_profitable)

least_profitable =  (df.groupby(by=['product_id','product_name'])
                  .agg(least_profitable = ('profit','sum'))
                  .nsmallest(10,columns=['least_profitable']))

print("\n least profitable products:")
print(least_profitable)


print("\n Sales by region:")
sales_region =  (df.groupby(by=['region'])
                  .agg(Total_Sales = ('sales','sum')).sort_values(by='Total_Sales',ascending=False))
print(sales_region)

print("\n Sales by category/sub-category:")
sales_category_sub_cat =  (df.groupby(by=['category', 'sub_category'])
                  .agg(Total_Sales = ('sales','sum')))
print(sales_category_sub_cat)

print("\n Profit per region/category:")
profit_region_cat =  (df.groupby(by=['region','category'])
                  .agg(Total_Profits = ('profit','sum')))
print(profit_region_cat)

