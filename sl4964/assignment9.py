'''
Created on Dec 2, 2016

This is the main project for assignment9.

@author: ShashaLin
'''

import pandas as pd
import os
from funcs import plot_year, merge_by_year, Region

cwd = os.getcwd()
countries = pd.read_csv(cwd + '/countries.csv')
income = pd.read_excel(cwd + '/indicator gapminder gdp_per_capita_ppp.xlsx',
                      index_col = 0).T
print(income.head())

year = 0
while year != 'finish':
    year = input('Enter a year to see income visualization. Enter \'finish\' to quit. ')
    try:
        year = int(year)
        if year not in income.index:
            print('Not valid year.')
        else:
            plot_year(year, income) 

    except ValueError:
        if year == 'finish':
            pass
        else:
            print('Not valid year.')
        
for year in range(2007, 2013):
    df_year= merge_by_year(year, income, countries)
    Region(year, df_year)


if __name__ == '__main__':
    pass
