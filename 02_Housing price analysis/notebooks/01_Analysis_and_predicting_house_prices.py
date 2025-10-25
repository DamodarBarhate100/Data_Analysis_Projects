import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading Housing Prices Data
housing_prices = pd.read_csv('datasets/Housing.csv')

# Data Cleaning
# we do not need lat and long columns so we are dropping them
housing_prices.drop(labels=['lat','long'],inplace=True,axis='columns')

# Converting data types
housing_prices['date'] = pd.to_datetime(housing_prices['date'],errors='coerce')
housing_prices['zipcode'] = housing_prices['zipcode'].astype('category')

# Replacing negative values with 0
numerical_columns = housing_prices.select_dtypes(['int','float'])
housing_prices[numerical_columns<0] = 0
print(housing_prices.head())

# Identying missing values
print("No. of missing values in each column:\n",housing_prices.isna().sum())
# No missing values in any column but for general purpose dropping it if any not detected
housing_prices.dropna(inplace=True)

# Dropping duplicate values
housing_prices.drop_duplicates(subset=['id'],inplace=True)
print("\n No. of duplicate values:\n",housing_prices.duplicated(subset=['id']).sum())


print(housing_prices.dtypes)