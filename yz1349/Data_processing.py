import pandas as pd
import matplotlib.pyplot as plt
'''
Created on Dec 3, 2016
@author: Yanli Zhou
'''

'''Loading datasets'''
def Load_data(name):
    if name == 'countries':
        countries = pd.read_csv('../countries.csv')
        return countries
    if name == 'income':
        income = pd.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx',index = 0)
        income = income.T
        income = income.rename(columns = income.iloc[0])
        income = income[1:] 
        return income
    
'''Loading histograms of income data for a specific year'''   
def Plot_data(year):
    plt.subplots(figsize=(10,10)) 
    income = Load_data('income')
    income.ix[year].dropna().hist()
    thistitle = 'Histogram of income of year '+str(year)
    plt.title(thistitle)
    plt.xlabel('Income per person')
    plt.ylabel('Count')
    plt.show()
    plt.close() 
    
'''Merging datasets of income and region of all countries by a given year'''    
def merge_by_year(year):
    income = Load_data('income')
    countries = Load_data('countries')
    if year not in income.columns:
        return ('No data for the year entered!')
    else:
        income_yr = pd.DataFrame(income.ix[year])
        year_data = pd.merge(countries,income_yr,left_on = 'Country',right_index =True)
        year_data.columns = ['Country','Region','Income']
        return year_data
    