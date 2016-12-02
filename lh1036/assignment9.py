# Author: Leslie Huang (lh1036)
# Description: Main

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from income.distribution import IncomeDistribution
from income.exceptions import *

# Read in the datasets
countries = pd.read_csv("countries.csv", index_col = "Country")
income = pd.read_excel("indicator gapminder gdp_per_capita_ppp.xlsx", index_col = "gdp pc test")

# transpose rows = years, cols = countries
income = income.transpose()

# Print head()
# print(income.head())

def quitting_input(prompt):
    '''
    Program will stop running if user types "finish," which raises QuitError
    '''
    userinput = input(prompt)
    
    if userinput == "finish":
        raise QuitError()
    
    return userinput

def prompt_for_year():
    '''
    Repeat prompting user for year until "finish" is entered.
    '''
    while True:
        try:
            userinput = quitting_input("Please enter a year or 'finish' when you are done.")
            return validate_year(userinput)
            
        except InvalidYearError as e:
            print(e, " Please enter a year or 'finish' when you are done.")

def validate_year(input_year):
    '''
    Validate that a year is in the income dataset
    '''
    try:
        year = int(input_year)
        
        if year not in income.index:
            raise InvalidYearError()
        
        else:
            return year
            
    except:
        raise InvalidYearError()
        

def plot_year_income(year, df=income):
    '''
    Return bar graph of each country's avg income/pc for a given year
    '''
    
    this_year = df.ix[year].dropna()
    year_plot = this_year.plot(kind = "barh", title = "Income by Country in {}".format(year))
    year_plot.set_xlabel("Income")
    plt.show()
    
    return year_plot

def merge_by_year(year, income, countries):
    '''
    Return DataFrame of income/pc for specified year, merging income and countries DFs
    '''
    merged = countries.join(income.ix[year], how = "outer")
    merged.reset_index(level = 0, inplace = True)
    
    return merged.rename(columns = {"index": "Country", year: "Income"})


# Runs the main program
if __name__ == "__main__":
    
    try:
        while True:
            year = prompt_for_year()
    
            # output all graphs for the given year
            this_year = IncomeDistribution(merge_by_year(year, income, countries), year)
            this_year.compare_within_region()
            this_year.compare_regional_income_spread()
            this_year.hist_within_region() 
    
    except (QuitError, KeyboardInterrupt):
        pass
            