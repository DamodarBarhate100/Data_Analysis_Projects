import pandas as pd
import numpy as np

# Loading Dataset

# Treating common missing strings as NaN values
df = pd.read_csv("data/superstores.csv", na_values=['NULL','NA','N/A',''])

print("Initial DataFrame:")
print(df.head(), "\n")

# Cleaning Column Names 
df.columns = df.columns.str.lower().str.replace(" ","_")

# Inspecting Data
print("DataFrame Info:")
print(df.info(), "\n")

print("Summary Statistics:")
print(df.describe(include='all'), "\n")

# Handling Missing Values 
str_cols = df.select_dtypes(include='object').columns
df[str_cols] = df[str_cols].apply(lambda x: x.str.strip())

# Convert order_date and ship_date to datetime
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce', dayfirst=True)
df['ship_date'] = pd.to_datetime(df['ship_date'], errors='coerce', dayfirst=True)

# convert the sales column into numeric
df['sales'] = pd.to_numeric(df["sales"],errors='coerce')

# Check missing values
print("Missing values before dropping:\n", df.isna().sum(), "\n")

# Drop rows where order_date or ship_date is missing
df.dropna(subset=['order_date', 'ship_date'], inplace=True)


print("Missing values after dropping essential NaNs:\n", df.isna().sum(), "\n")

# Handling Duplicates 
print("Number of duplicate rows before dropping:", df.duplicated().sum())
df.drop_duplicates(inplace=True)
print("Number of duplicate rows after dropping:", df.duplicated().sum(), "\n")

print("\nChecking any duplicate values in the order_id column as it need to be unique:")
print("Number of duplicate rows before dropping in order_id column:", df.duplicated(subset=['order_id']).sum())
df.drop_duplicates(subset=['order_id'],inplace=True)
print("Number of duplicate rows after dropping in order_id column:", df.duplicated(subset=['order_id']).sum(), "\n")



#  Final Checks 
print("DataFrame info after cleaning:")
print(df.info(), "\n")

print("DataFrame shape after cleaning:", df.shape, "\n")

print("First 5 rows after cleaning:")
print(df.head())

df.to_csv("data/cleaned_superstore_sales.csv",index=False)