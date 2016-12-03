# Author: Leslie Huang (lh1036)
# Description: Helper functions to prompt and handle userinput of year in the "main"

from income.distribution import IncomeDistribution
from income.exceptions import *

### Helper functions to prompt and handle user input of year
def quitting_input(prompt):
    '''
    Program exits if user types "finish," which raises QuitError
    '''
    userinput = input(prompt)
    
    if userinput == "finish":
        raise QuitError()
    
    return userinput

def prompt_for_year(income):
    '''
    Prompt user for year. Repeats prompt until "finish" is entered.
    @param income: income DF containing data from the year specified
    
    '''
    
    while True:
        try:
            userinput = quitting_input("Please enter a year or 'finish' when you are done.")
            return validate_year(userinput, income)
            
        except InvalidYearError as e:
            print(e, " Please enter a year or 'finish' when you are done.")

def validate_year(input_year, income):
    '''
    Validate that user input is a valid year from the income dataset
    Raises InvalidYearError if (1) input type is invalid (e.g. string or float) 
    or (2) year is not in data
    
    @param input_year: user-provided year to be validated
    @param income: income DF containing data from the year specified
    '''
    
    try:
        year = int(input_year)
        
        if year not in income.index:
            raise InvalidYearError()
        
        else:
            return year
            
    except ValueError:
        raise InvalidYearError()
        