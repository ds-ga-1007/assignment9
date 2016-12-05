import pandas as pd
import matplotlib.pyplot as plt

countries = pd.read_csv("countries.csv")
income = pd.read_csv("indicator gapminder gdp_per_capita_ppp.csv", index_col = 0)
income = income.T

#Print head of income dataset when loaded
print(income.head())
            
def plot_year(data, year):
    
    '''
    Function plot_year display the distribution of income per person across all countries in the world for the given year.
    
    parameters:
        data:    income
        year:    given year
    
    return:
        histogram of income per person in given year
    '''
    
    plt.hist(data.ix[year-1800].dropna(), alpha=0.9, color='blue')  # Tried using year as index, but it seemed that the index is count begin with 1800
    plt.title("Histogram of income per person in year " + str(year))
    plt.xlabel("Income")
    plt.ylabel("Frequency")
    plt.show()

    
def merge_by_year(year):
    
    '''
    Function merge_by_year merge the countries and income data sets for any given year. 
    
    parameters:
        data1:    countries
        data2:    income
        year:    given year
        
    return:
        DataFrame with three columns: Country, Region, and Income
    '''
    
    yearincome = income.ix[[year-1800]].T   # Same problem as function plot_year shows
    yearincome.columns = ['Income']
    yearincome['Country'] = yearincome.index
    merge = pd.merge(countries, yearincome, on = 'Country', how = 'left')
    return merge