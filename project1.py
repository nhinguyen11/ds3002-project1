#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DS 3002 Project 1
By: Nhi Nguyen (nyn4tv)
"""

import pandas as pd
import json 
import csv
import numpy as np

#%%
# Benchmark 1.1: Retrieve a local file
directory = "./Netflix subscription fee Dec-2021.csv"

try:
    netflix = pd.read_csv(directory)
    print(netflix)
except FileNotFoundError:
    print("Your input file is not a csv or your input is invalid.")
    
# Benchmark 1.5: Generate a brief summary of the data file
numcol = len(netflix.columns)
numrow = len(netflix)
print("Number of records:",numcol)
print("Number of rows:",numrow)
print(" ")
print("The first five rows of the data set:")
print(netflix.head(5))


#%%
# Benchmark 1.3: Modify the number of columns from the source to the destination, reducing or adding columns.
netflix_new = netflix.copy()

# If library size <= 2500, users should get basic plan.
# If library size > 2500 but <= 5000, users should get standard plan.
# If library size > 5000, users should get the premium plan.
conditions = [
    (netflix_new['Total Library Size'] <= 2500),
    (netflix_new['Total Library Size'] > 2500) & (netflix_new['Total Library Size'] <= 5000),
    (netflix_new['Total Library Size'] > 5000)]

values = ['Basic', 'Standard', 'Premium']

netflix_new['Recommended Plan'] = np.select(conditions, values) # returns an array based on conditions --> new column
netflix_new.to_csv('./netflix_new.csv')
print(netflix_new.head(5))


#%%
# Benchmark 1.2: Convert the general format and data structure of the data source.

# CSV to JSON
csvfile = open('./Netflix subscription fee Dec-2021.csv', 'r')
jsonfile = open('./JSONnetflix.json', 'w')

fieldnames = ("Country Code","Total Library Size","No.of TV Shows","No.of Movies","Country","Cost Per Month - Basic ($)","Cost Per Month - Standard ($)","Cost Per Month - Premium ($)")
reader = csv.DictReader(csvfile,fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
    json.dumps(row, sort_keys=False, indent=4, separators=(',', ': ')) # commas and colon to make it easier to read


#%%
# Benchmark 2: The processor should produce informative errors should it be unable to complete an operation.
netflix_country = netflix.copy() 
netflix_country['Country'] = netflix_country['Country'].str.lower() # lower case the country column for matching later on

# I recommend inputing a random symbol or "China" (not in the data set) in order to see the error message.
try:
    country_input = input("Please input a country to find plans & pricing: ")
    country_input_clean = country_input.lower().strip()  # lower case and strip white space off the input
    if (netflix_country['Country'] == country_input_clean).any():
        print("Country:",netflix['Country'].loc[netflix_country['Country'] == country_input_clean].to_string(index=False)) # to_string(index=False) to get rid of dtype and index value for prettier output
        print("Basic Plan:",netflix['Cost Per Month - Basic ($)'].loc[netflix_country['Country'] == country_input_clean].to_string(index=False)) 
        print("Standard Plan:",netflix['Cost Per Month - Standard ($)'].loc[netflix_country['Country'] == country_input_clean].to_string(index=False))
        print("Premium Plan:",netflix['Cost Per Month - Premium ($)'].loc[netflix_country['Country'] == country_input_clean].to_string(index=False))
    elif (netflix_country['Country'] != country_input_clean).any():
        raise Exception("ERROR: Country not in system or input is invalid")  # raising an exception for error line
except Exception:
    print("ERROR: Country not in system or input is invalid")
    
    
    
    
    
    
    