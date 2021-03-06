import pandas as pd
from dataTool import *
import sys
'''
Created on Nov 30, 2016

@author: peimengsui
@desc: this program runs a user interactive data analysis tool on income country dataset
'''

if __name__ == '__main__':
    countries = pd.read_csv('countries.csv',index_col=0)
    income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',index_col=0)
    income_transpose = income.T
    print(income_transpose.head())
    while(True):
        try:
            year = input("Please enter the year between 1800 and 2012, or 'Finish': ")
            if year == 'Finish':
                for y in range(2007, 2013, 1):
                    merged = merge_by_year(countries, income, y)
                    tools = dataTool(y,merged)
                    tools.boxplot()
                    tools.histogram()
                print('Finish!')
                sys.exit(0)
            elif year.isdigit() and int(year) >= 1800 and int(year) <= 2012:
                year = int(year)
                visual_income_dist(year,income)
            else:
                print ('invalid year')
        except KeyboardInterrupt:
            sys.exit(1)