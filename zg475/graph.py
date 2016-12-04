'''
This module contains two methods.
One is plot the histogram of income for a give year.
Another is the merge method, which will merge the countries and income data sets for any given year.

Created on Dec 3, 2016
@author: Zhiqi Guo(zg475)
@email: zg475@nyu.edu
'''

from data_process import load_data
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('fivethirtyeight')

def plot_income(year):
    fig, ax = plt.subplots(figsize=(10,10)) 
    income = load_data('income')
    income.ix[year].dropna().hist()
    ax.set_title('Histogram of income for year '+str(year))
    ax.set_xlabel('Income per person')
    ax.set_ylabel('Count')
    fig.savefig('Histogram of income for year '+str(year)+'.pdf')
    plt.show()
    plt.close() 

def merge_by_year(year):
    '''
    Merge the countries and income data sets for any given year. 
    '''
    income = load_data('income')
    countries = load_data('countries')
    income_yr = pd.DataFrame(income.ix[year])
    col_name = ['Country','Region','Income']
    newdf = pd.merge(countries,income_yr,left_on = 'Country',right_index =True)
    newdf.columns = col_name
    return newdf
