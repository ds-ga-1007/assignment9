'''
Created on Dec 4, 2016

@author: Christine
'''
import pandas as pd
import sys
from analysis import *

'''
load the countries.csv file
Load the indicator gapminder gdp_per_capita_ppp.xlsx data set
Transform the data set to have years as the rows and countries as the
columns, then show the head of this data set when it is loaded
'''
countries = pd.read_csv('countries.csv')
income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx').transpose()
income.columns = [income.ix[0]]
income = income.drop(['gdp pc test'],axis=0)
print('The head of income dataset:')
print(income.head())

'''
The program asks the user to enter a year, then display the distribution of income per person for that year
until 'finish' is typed.
Then, use the class analysis to generate graphs for the years 2007-2012
'''
while True:
    try:
        year_input = input('Enter a year(type finish to quit):')
        if year_input.lower() == 'finish':
            for year in range(2007,2013):
                merged_df = merge_by_year(year,income,countries)
                plot = analysis(merged_df,year)
                plot.histogram()
                plot.boxplot()
            sys.exit()
        if int(year_input) not in income.index:
            raise InvalidInput
        else:
            year = int(year_input)
            distr_income(income, year)
    except KeyboardInterrupt:
        sys.exit(0)
    except EOFError:
        sys.exit(0)
    
    
    
    
    
    
    
    