import pandas as pd
from Data_tool import *
from Data_processing import *
import sys

'''
Created on Dec 4, 2016
@author: Yanli Zhou
This is the main program that asks the user to input a year from 1800 t 2012 and displays the histogram of income per person 
for the given year. It will keep propting the user for input until the string "finish" is entered. The program 
then uses the class Data_tool to generate and save histograms and boxplots for the years 2007-2012
'''

if __name__ == '__main__':
    income = countries = Load_data('income')
    while True:
        try:
            year = input("Please enter an year between 1800 and 2012, or enter 'finish': ")
            if year == 'finish':
                for y in range(2007,2013):
                    thistool = Data_tool(y)
                    thistool.boxplot()
                    thistool.histogram()
                sys.exit(0)
            elif year.isdigit() and int(year) >= 1800 and int(year) <= 2012:
                year = int(year)
                Plot_data(year)
            else:
                raise ValueError
        except ValueError:
            print('Invalid year input')
        except KeyboardInterrupt:
            sys.exit(1)