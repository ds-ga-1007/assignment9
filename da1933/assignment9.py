'''
Created on Dec 2, 2016

This program follows all of the steps of DS-GA-1007 Assignment 9 according to the instructions listed.

I relied on class notes and the following references for clues to data manipulation
and visualization  
http://pandas.pydata.org/pandas-docs/version/0.18.1/visualization.html
http://pandas.pydata.org/pandas-docs/version/0.17.1/generated/pandas.DataFrame.set_index.html
http://pandas.pydata.org/pandas-docs/stable/generated/pandas.concat.html
@author: da1933 (Daniel Amaranto)
'''

from graph_functions import income_distribution
from analysis_tools import Region
import pandas as pd


def main():
    print(income.head())
    years = list(income.index[:])
    complete = False
    while complete is not True:
        choice = input('Please select a year: ')
        if choice == 'finish':
            complete = True
        else:
            try:
                if int(choice) in years:
                    income_distribution(int(choice))
                else:
                    print('No data for that year.\n')
            except ValueError:
                print("That's not a year.\n")
                choice = None
    
    regions = list(countries.Region.drop_duplicates())
    recent_five_years = list(range(2007,2013,1))
    for region in regions:
        for year in recent_five_years:
            temp = Region(str(region))
            temp.save_graphs(year)

if __name__ == '__main__':
    countries = pd.read_csv('countries.csv')
    income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',index_col=0).transpose()
    income.columns.name = 'Country'
    main()

