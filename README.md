# DS 3002 Project 1
Nhi Nguyen (nyn4tv)

## Data Description:
My data of choice comes from Kaggle and it has information on the Netflix library sizes and pricing plans for a number of countries. There are 65 countries in total and for each country, there's data on the country's Netflix total library size, total number of TV shows, total number of movies, price for basic plan, price for standard plan, and price for premium plan. There's also a column named "Country Code" with the identifiers for each country.

Source: https://www.kaggle.com/prasertk/netflix-subscription-price-in-different-countries/version/2?select=Netflix+subscription+fee+Dec-2021.csv

## How It Works:
1. The program ingests a local file (Netflix subscription fee Dec-2021.csv) and outputs it if it's the correct data structure. If not, it will output an error message asking the user if their input matches with the requirements. 
2. The program prints a few lines of text to describe the dataset. The first line is the number of records (columns) and the second line is the number of rows. The third line and on are the first fives rows of the data set. 
3. A new data set exports here with a new column. The newest column is named "Reccomended Plan" and it reccomends to users the Netflix plan they should pick depending on the total library size in their respective countries. In addition to the "Reccomended Plan" column, the new data set has all of the columns from the original data set. The new data set is named "netflix_new.csv" (attached above).
4. The original netflix data set converts to a JSON file. The new JSON file is named "JSONnetflix.json" (attached above).
5. This last part uses try/except statements to produce informative errors when running into issues. The program will ask the user to input a country name in which it will use to shift through the data set. If the user inputs a country that matches with a row in the data set, the program will out the country name and the prices of all the plans (basic, standard, and premium). If the user inputs something that doesn't match (e.g. "china" or "United State") or something invalid (e.g. "1234#@" or a non-string), the program will output an error message.

## Meeting Benchmarks:
1. The program ingests a local file (csv).
2. The program prints a brief summary of the data set.
3. The program adds another column to the data set and exports that new data set.
4. The program converts the csv file to a JSON file. 
5. The program takes in user input and matches it with the data set. If the input is invalid, then an informative error message outputs.

