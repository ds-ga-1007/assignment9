'''
Author: lg2755
Date: Dec 03, 2016
DS_1007 Assignment 9

This is the main program for assignment 9.
'''
from incomeclass import *

# Load the "countries.csv" as a pandas DataFrame
countries = pd.read_csv('../countries.csv')

# Load and transpose the excel data set as income
income = pd.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx', index_col=0).transpose()
# Take a look at the head of the DataFrame
income.head()

# Ask the user to input a year
while True:
    inputStr = input('Please enter a year between 1800 to 2012, both are inclusive. \n')
    if inputStr == 'finish':
        break
    else:
        try:
            # check user input
            len(inputStr) == 4
            inputYear = int(inputStr)
            (inputYear >= 1800) and (inputYear <= 2012)
        except InputValueException:
            print('The input has to be four digits between 1800 to 2012, inclusive')
        displayIncomeDistribution(inputYear, income)

# Generate EDA plots figures for income per person between 2007 and 2013 by region
for year in range(2007, 2013):
    oneyeardata = mergeByYear(year, income, countries)
    oneyearplot = ExploreDistribution(oneyeardata)
    oneyearplot.generateHistogram()
    oneyearplot.generateBoxplots()
