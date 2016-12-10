import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

f1='../countries.csv'
f2='../indicator gapminder gdp_per_capita_ppp.xlsx'
countries = pd.read_csv(f1, index_col = 0)
income = pd.read_excel(f2, index_col = 0)
income = income.transpose()

 

def merge_by_year(year):
    '''
    with a given year, the function will merge the countries and income data set
    '''
    
    df1 = countries 
    df1['Country'] = list(countries.index)
    year_data = income.loc[year,:]
    df2 = year_data.to_frame()
    df2['Country'] = list(df2.index)
    result = pd.merge(df1,df2, on='Country')
    return result

    
def income_by_year(year):
    '''
    for a given year, the function will graphically display the distribution of income per person across all countries 
    '''
    
    year_data = income.loc[year,:]
    y_pos = np.arange(len(year_data.dropna()))
    plt.ylim(0, len(year_data))
    countriesNames = pd.Series(year_data.index.values, dtype='category')
    plt.yticks(y_pos, countriesNames, size=7)
    plt.title('distribution of income per person across all countries_' + str(year))
    plt.barh(y_pos, year_data.dropna())
    plt.show