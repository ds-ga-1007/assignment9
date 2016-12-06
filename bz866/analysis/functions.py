'''
Created on 2016年12月4日

@author: bz866
'''

import pandas as pd
import matplotlib.pyplot as plt


def read_data():
    '''
    load data and show column names
    '''
    countries = pd.read_csv('countries.csv')
    income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx', index_col = 0)
    income_transpose = income.T
    print(income_transpose.head())
    return countries, income

def merge_by_year(year, countries, income):
    '''
    merge_by_year
    '''
    income_one_year = pd.DataFrame(income[year])
    merged_data = pd.merge(countries, income_one_year, left_on='Country', right_index=True)
    merged_data = merged_data.dropna()
    merged_data.columns = ['Country', 'Region', 'Income']
    return merged_data

def show_distribution(income, year):
    '''show distribution figure in a new window according Users' input'''
    income[year].dropna().plot(kind = 'hist')
    plt.title("Histogram of graphically distribution of the income per person in " + str(year))
    plt.xlabel('Income per person')
    plt.ylabel('Count')
    plt.show()
    
    '''close the window for next input'''
    plt.close() 
    
    
    