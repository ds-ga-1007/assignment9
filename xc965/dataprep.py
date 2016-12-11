'''
This module prepares and manipulates data sets to serve further visualizations.

@author: Xianzhi Cao (xc965)
'''

import pandas as pd
import os


def data_prep():
    '''
    prepare and clean the data sets
    '''
    # read and load countries.csv as DataFrame
    countries = pd.read_csv('../countries.csv')
    # read and load gdp_per_capita_ppp.xlsx as DataFrame
    income_raw = pd.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx',
                               index_col='gdp pc test')
    # transform the data set to have years as the rows and countries as the columns
    income = income_raw.T

    return countries, income


def merge_by_year(year):
    '''
    merge the countries DataFrame and income DataFrame by the given year
    '''
    countries, income = data_prep()  # get two DataFrames

    income_by_year = pd.DataFrame(income.loc[year, :])  # get all countries' incomes by given year
    income_by_year.reset_index(inplace=True)  # reset index
    income_by_year.columns = ['Country', 'Income']  # rename columns
    merged_income_by_year = pd.merge(countries, income_by_year, on='Country')  # inner merge two DataFrames by 'Country'
    return merged_income_by_year
