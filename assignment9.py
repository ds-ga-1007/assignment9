'''
@author: jonathanatoy
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import matplotlib
import seaborn
import world_Income_per_capita

class YearException(Exception):
    def __str__(self):
        out = 'This is not a valid year between 1800 and 2012. Exception!'
        return out

def show_income_dist_by_year(income_df, year):
    '''
    Plots a histogram of per capita income for the given year.
    '''
    pl.figure(figsize = (8,8))
    income_df.ix[year].hist()
    pl.xlabel('Income per Capita', fontsize = 18)
    pl.ylabel('Worldwide Incidence', fontsize = 18)
    pl.title('Distribution of Per Capita Income in ' + str(year), fontsize = 18)
    pl.show()

def merge_by_year(income, countries, year):
    '''
    Merges income and country DataFrames for a particular year.
    '''
    year_income = pd.DataFrame(income.transpose()[year]).rename(index = str, columns = {year : 'Income'})
    worldwide_year_income = pd.merge(countries, year_income, how='inner', left_on='Country', right_index=True)
    return worldwide_year_income

def validYearCheck(input_year):
    '''
    Checks whether input values are valid integer years between 1800 and 2012.
    '''
    try:
        year = int(input_year)
        if year < 1800:
            raise YearException
        elif year > 2012:
            raise YearException
    except ValueError:
        raise YearException
    return year

def main():
    '''
    Main program designed to plot the histogram of per capita income distribution across .
    countries per year. The user is asked to specify a year between 1800 and 2012 to examine
    until 'finish' is typed. The histogram and boxplots of income distribution by region
    are then generated for the most recent years in the data (2007-2012).
    '''
    
    print('Reading in countries.csv...')
    countries = pd.read_csv('countries.csv')
    
    print('Reading in indicator gapminder gdp_per_capita_ppp.xlsx...')
    income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx', index_col='gdp pc test').transpose()
    
    print('Printing head() of income...')
    print(income.head())
    
    input_line = input("Enter a year between 1800 and 2012: ")
    try:
        year = validYearCheck(input_line)
        show_income_dist_by_year(income, year)
    except YearException:
        print('Invalid Year')
    
        
    
    while True:
        input_line = input("Enter another year? (type 'finish' if finished) ")
        if input_line == 'finish':
            break
        try:
            year = validYearCheck(input_line)
            show_income_dist_by_year(income, year)
        except YearException:
            print('Invalid Year')
        
    
    print('Now plotting income distribution by region for 2007-2012 as PDFs')
    for year in [2007, 2008, 2009, 2010, 2011, 2012]:
        world_Income_1yr = world_Income_per_capita.world_Income_per_capita(income, countries, year)
        world_Income_1yr.income_dist_byRegion_box()
        world_Income_1yr.income_dist_byRegion_hist()
        print('Year ' + str(year) + ': finsihed!')
    print('Now exiting program.')
    
    
if __name__ == '__main__':
    main()