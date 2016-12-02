# Author: Leslie Huang (lh1036)
# Description: Main

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from income.distribution import IncomeDistribution

# Read in the datasets
countries = pd.read_csv("countries.csv", index_col = "Country")
income = pd.read_excel("indicator gapminder gdp_per_capita_ppp.xlsx", index_col = "gdp pc test")

# transpose rows = years, cols = countries
income = income.transpose()

# Print head()
# print(income.head())

def plot_year_income(year, df=income):
    '''
    Return bar graph of each country's avg income/pc for a given year
    '''
    
    this_year = df.ix[year].dropna()
    year_plot = this_year.plot(kind = "barh", title = "Income by Country in {}".format(year))
    year_plot.set_xlabel("Income")
    plt.show()
    
    return year_plot

# plot_year_income(2012)

def merge_by_year(year, income, countries):
    '''
    Return DataFrame of income/pc for specified year, merging income and countries DFs
    '''
    merged = countries.join(income.ix[year], how = "outer")
    merged.reset_index(level = 0, inplace = True)
    
    return merged.rename(columns = {"index": "Country", year: "Income"})
    
year = 2012
id = IncomeDistribution(merge_by_year(year, income, countries), year)
# id.compare_within_region()

id.hist_within_region()

# id.compare_regional_income_spread()