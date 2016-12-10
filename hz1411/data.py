'''This module define 3 functions that loads data into dataframe, plot histograms and merge them by year separately'''

import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    '''load data file into Pandas Dataframe, make transformations and return the dataframe'''
    countries = pd.read_csv('../countries.csv')
    income = pd.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx',index_col=0)
    income = income.T
    print(income.head())
    return countries, income

countries,income = load_data()
def income_distribution(year):
    '''this function draws a histogram to display the distribution of 
    income per person across all countries in the world for the given year'''
    income_year = income.ix[year].dropna()
    income_year.hist()
    plt.title('Income distribution of all countries in '+str(year))
    plt.xlabel('Income per capita')
    plt.ylabel('Count')
    plt.show()

def merge_by_year(year):
    '''Merge the countries and income data sets for any given year'''
    income_year_df = pd.DataFrame(income.ix[year])
    merged = pd.merge(countries,income_year_df, left_on = 'Country',right_index=True)
    merged = merged.rename(columns = {year:'Income'})
    return merged
