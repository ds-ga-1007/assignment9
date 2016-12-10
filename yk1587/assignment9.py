'''
Created on Dec 4 2016

@author: keyaohan
'''

'''
This program first load the countries and income data sets and transform the income
data and print out its head. Then it ask the user to input year in the interval of 
[1800,2012] and plot the histogram of the income per person across all countries in 
the world for the given year and also plot the boxplots and histograms of the income 
per person of across regions. All figures will be saved in .pdf files.
'''

import pandas as pd
from income.income_class import *
from income.functions import *
from income.exceptions import *

# print the transformed DataFrame (from functions.py) to show the head of this data set
print(trans_income.head())

while True:
    try:
    # Continue asking the user for a year and displaying the graph until 'finish' is entered.
        yearInput = input('Please enter a year. (Enter "finish" to quit) \n')
        yearInput = check_validity(yearInput)
        plot_incomeList(yearInput)
        income_plots(yearInput).plot_box()
        income_plots(yearInput).plot_hist()
            
    except BreakException:
        break
    except IntegerError:
        print('The input year should be an integer. Please enter again.')
    except RangeError:
        print('The input year should be in the interval [1800, 2012]. Please enter again.')

if __name__ == '__main__':
    pass