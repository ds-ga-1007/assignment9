'''
Created on Dec 5, 2016

@author: sj238
'''
import pandas as pd
import matplotlib.pyplot as plt


''' 
Read 'countries.csv'.
Read 'indicator gapminder gdp_per_capita_ppp.xlsx' transpose so that years become the rows and countries become the columns
'''
countries = pd.read_csv('countries.csv')
income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',index_col=0).transpose()
income.columns.name = 'Country'
    
def incomeDistribution(year):
    '''
    This function shows income per person distribution
    of each country for a given year using vertical bar plot.
    '''
    # Referance: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html
    income.ix[year].plot(kind='bar',figsize=(100,100),width = 1.0)
    plt.title('Distribution of income per person across all countries in the world for year ' + str(year))
    plt.xlabel('Countries')
    plt.ylabel('Income per person')
    plt.show()
    plt.close()


def merge_by_year(year):
    '''
    This function merges the countries and income data sets for any given year
    '''
    data = income.transpose().reset_index()
    merged = pd.merge(countries, data, on='Country')
    by_year = merged.loc[:,['Country', 'Region', year]]
    by_year.columns.values[[2]] = ['Income']
    return by_year
   


