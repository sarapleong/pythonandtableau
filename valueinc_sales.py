#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 15:32:53 2023

@author: saraleong
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') <-- FORMAT of read_csv

data = pd.read_csv('transaction2.csv')

data = pd.read_csv('transaction2.csv', sep=';')

# summary of the data
data.info()

# working with calculations

# defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

# Mathematical Operations on Tableau

ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem
SellingPricePerTransaction = SellingPricePerItem * NumberOfItemsPurchased
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

# CostPerTransaction Column Calculation

# CostPerTransaction = CostPerItem * NumberOfItemsPurchased
# variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

# Adding new column to a dataframe

data['CostPerTransaction'] = CostPerTransaction

# Sales Per Transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

# Profit Calculation = Sales - Cost

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

# Markup = (sales - cost) / cost

data['Markup'] = (data['ProfitPerTransaction']) / data['CostPerTransaction']

# Rounding Markup with ound() function

RoundMarkup = round(data['Markup'], 2)

data['Markup'] = round(data['Markup'], 2)

# combining data fields

# my_date = data['Day'] + '-'

# checking columns data type
print(data['Day'].dtype)

# change columns type

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day + '-' + data['Month'] + '-' + year

data['date'] = my_date

# using iloc to view specific columns/rows

data.iloc[0] #views the row with index = 0
data.iloc[0:3] #first 3 rows 
data.iloc[-5:] # last 5 rows

data.head(5) #brings in first 5 rows

data.iloc[:,2] #brings in all rows in 2nd column

data.iloc[4,2] #brings in 4th row, 2nd column

# using split() to split the client keywords field
# new variable = column.str.split('se', expand = True)

split_col = data['ClientKeywords'].str.split(',', expand = True)

# creating new columns for the split columns in Client Keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

# using replace function

data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']','')

# using the lower() function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

# how to merge files

# bringing in new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

# merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

# dropping columns

# df = df.drop('columnname', axis = 1)
data = data.drop('ClientKeywords', axis = 1)

data = data.drop('Day', axis = 1)

data = data.drop(['Year', 'Month'], axis = 1)

# export into CSV

data.to_csv('ValueInc_Cleaned.csv', index = False)
