import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load countries and income
countries = pd.DataFrame.from_csv('countries.csv', index_col = None)

income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx') 
income = income.T
column_name = income.iloc[0] 
income = income[1:] 
income.columns = column_name
    
print('Income is loaded.')

def year_valid(year):
    """
    To check if the input is a year between 1800 - 2012.
    """
    if year < 1800 or year > 2012:
        raise ValueError("Input num_trials should between 1800 - 2012.")
    return(year)

def ppp(income, year):
    """
    Histogram of ppp across all countries in a given year.
    """
    data_by_year = income.iloc[year - 1800]
    data_cleaned = data_by_year[np.logical_not(np.isnan(list(data_by_year)))]
    plt.hist(data_cleaned,25)
    plt.title('The distribution of ppp across all countries in ' + str(year))
    plt.show()
    
def merge_by_year(income, countries, year):
    """
    Merge the countries and income data sets for any given year.
    """
    data_by_year = pd.DataFrame(income.iloc[year - 1800])
    data_by_year['Country'] = income.columns
    merge = pd.merge(countries, data_by_year, on = 'Country')
    merge.columns = ['Country', 'Region', 'Income']
    merge.Income = merge.Income.astype(float)
    return merge
    