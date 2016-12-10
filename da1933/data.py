'''
Created on Dec 2, 2016

@author: da1933
'''

import pandas as pd

def load_data(data):
    if data =='country':
        return pd.read_csv('countries.csv')
    elif data =='income':
        income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',index_col=0).transpose()
        income.columns.name = 'Country'
        return income
