# Author: Leslie Huang (lh1036)
# Description: Main program to interact with user and generate graphs

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from income.distribution import IncomeDistribution
from income.exceptions import *

### Importing and setting up the data

# Questions 1-2: Read in the datasets
countries = pd.read_csv("countries.csv", index_col = "Country")
income = pd.read_excel("indicator gapminder gdp_per_capita_ppp.xlsx", index_col = "gdp pc test")

# Question 3: transpose rows = years, cols = countries
income = income.transpose()

# Question 3: print head() of data
print("Per question #3, view the head of the transformed income dataset.")
print(income.head())

### Helper functions to prompt and handle user input of year
def quitting_input(prompt):
    '''
    Program exits if user types "finish," which raises QuitError
    '''
    userinput = input(prompt)
    
    if userinput == "finish":
        raise QuitError()
    
    return userinput

def prompt_for_year():
    '''
    Prompt user for year. Repeats prompt until "finish" is entered.
    '''
    
    while True:
        try:
            userinput = quitting_input("Please enter a year or 'finish' when you are done.")
            return validate_year(userinput)
            
        except InvalidYearError as e:
            print(e, " Please enter a year or 'finish' when you are done.")

def validate_year(input_year):
    '''
    Validate that user input is a valid year from the income dataset
    Raises InvalidYearError if (1) input type is invalid (e.g. string or float) 
    or (2) year is not in data
    '''
    
    try:
        year = int(input_year)
        
        if year not in income.index:
            raise InvalidYearError()
        
        else:
            return year
            
    except:
        raise InvalidYearError()
        
### Function to generate dataframe for a specified year, for use in constructing IncomeDistribution objects. This function does not belong in a separate class
def merge_by_year(year, income, countries):
    '''
    Question 5: Return properly labeled DataFrame of income/pc per country for a specified year.
    Merges income and countries DFs
    NOTE: I choose to pass the DFs to be merged (income and countries) as additional parameters
    to allow flexible use of this function in other settings
    '''
    
    merged = countries.join(income.ix[year], how = "outer")
    merged.reset_index(level = 0, inplace = True)
    
    return merged.rename(columns = {"index": "Country", year: "Income"})


### Runs the main program
if __name__ == "__main__":
    
    try:
        while True:
            year = prompt_for_year()
    
            # Question 7: Output graph for the year entered by the user
            this_year = IncomeDistribution(merge_by_year(year, income, countries), year)

    
    except (QuitError, KeyboardInterrupt):
        pass
        
        # Question 8: Use all graphing methods created in Question 6 to produce graphs for 2007-2012
        years = range(2007, 2013)
        
        for this_year in years:
            this_year.plot_world_income_for_year()
            this_year.compare_within_region()
            this_year.compare_regional_income_spread()
            this_year.hist_within_region()
            