'''
Created on 2016.12.2.

This is used for reading the data and print the head

@author: xulei
'''


import pandas as pd
import matplotlib.pyplot as plt
countries=pd.read_csv('countries.csv')
income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',index_col='gdp pc test')
income=income.T


income.head()

def draw_bar_by_counties(year):
    df=income.ix[year]
    df.hist()
    plt.show()
    
#draw_bar_by_counties(1801)
def merge_by_year(year):
    df=income.ix[year]
    df.name='Income'
    merged=countries.join(df, on='Country')
    return merged


