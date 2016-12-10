'''
Created on Dec 2, 2016

@author: da1933
'''

import matplotlib.pyplot as plt
import pandas as pd

countries = pd.read_csv('countries.csv')
income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',index_col=0).transpose()
income.columns.name = 'Country'

    #As per the instructions, this function represents income distribution
    #across the world for a given year.  Unfortunately, there are so many 
    #countries that the output can seem cramped, depending on what
    #you are using to generate the visualizations.
     
def income_distribution(year):
    income.ix[year].plot(kind='barh',figsize=(10,100),width = 1.0)
    plt.show()
    
    
    #This function merges the two datasets into the proper format
def merge_by_year(year):
    data = income.transpose().reset_index()
    merged = pd.merge(countries, data, on='Country')
    by_year = merged.loc[:,['Country', 'Region', year]]
    by_year.columns.values[[2]] = ['Income']
    return by_year