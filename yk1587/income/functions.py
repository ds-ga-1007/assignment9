import pandas as pd
import matplotlib.pyplot as plt
from income.exceptions import *

# load the countries.csv file into pandas DataFrame and name as countries
countries = pd.read_csv('/Users/keyaohan/git/assignment9/countries.csv')
# load the indicator gapminder gdp_per_capita_ppp.xlsx data set into a DataFrame called income
income = pd.read_excel('/Users/keyaohan/git/assignment9/indicator gapminder gdp_per_capita_ppp.xlsx', index_col=0)

income.index.name = 'Country'  # give the income DataFrame an index name as 'Country'
income.columns.name = 'Year'  # give the income DataFrame a column name as 'Year'

# transform the income DataFrame to have years as the rows and countries as the columns
trans_income = income.T

def check_validity(yearInput):
    '''This function checks if the user input is correct as a year in [1800,2012]. Invalid
inputs would cause exceptions.'''
    if yearInput == 'finish':
        raise BreakException()  # Input 'finish' would quit the program.
    elif yearInput.isdigit() == False:
        raise IntegerError()  # If the input is not a valid integer an IntegerError would be raised.
    elif int(yearInput) not in range(1800,2013):
        raise RangeError()  # If the year input is not in [1800,2012] a RangeError would be raised.
    else:
        return yearInput  # Valid input would be returned.
    
def plot_incomeList(year):
    '''This function is used to plot the histogram of the income per person across all
countries in the world for a given year to graphically display its distribution.'''
    year = int(year)
    cleanList = trans_income.loc[trans_income.index == year].dropna(axis=1).iloc[0,:]
    plt.clf()
    cleanList.hist(bins=50)
    plt.title('Histogram across All Countries for the Year ' + str(year))
    plt.xlabel('Income')
    plt.ylabel('Frequency')
    plt.savefig('Distribution of IncomeList_' + str(year) + '.pdf')
    
def merge_by_year(year):
    '''This function is used to merge the countries and income data sets for a given year.
It returns a result as a DataFrame with three columns titled Country, Region and Income.'''
    year = int(year)
    merged_df = pd.merge(countries, income, left_on='Country', right_index=True)
    grouped_df = merged_df[['Country', 'Region', year]].rename(columns={year: 'Income'})
    return grouped_df