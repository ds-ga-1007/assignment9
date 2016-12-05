import pandas as pd
import matplotlib.pyplot as plt

def loadData():
    """
    Load the two data files, countries and income, and print the head of income
    """
    countries = pd.read_csv('countries.csv')
    income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',index_col=0)
    income = income.T
    print(income.head())
    return countries, income

countries,income = loadData()

def income_dist(year):
    '''this function draws a histogram to display the distribution of 
    income per person across all countries in the world for the given year'''
    incomeYear = income.ix[year].dropna()
    incomeYear.hist()
    plt.title('Income Distribution For All Countries: '+str(year))
    plt.xlabel('Income Per Person')
    plt.ylabel('Frequency')
    plt.show()

def merge_by_year(year):
    '''Merge the countries and income data sets for any given year'''
    income_year = pd.DataFrame(income.ix[year])
    merged = pd.merge(countries,income_year, left_on = 'Country',right_index=True)
    merged = merged.rename(columns = {year:'Income'})
    return merged
