'''
Created on Dec 5, 2016

@author: Yovela
'''

'''
this is the main function for assignment9
'''
import sys
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from classes import *
from functions import *

# load the countries.csv file into a pandas DataFrame and name this data set "countries"
countries = pd.read_csv("countries.csv", sep=',')

# load the "indicator gapminder gdp_per_capita_ppp.xlsx" data set into a DataFrame called income
# transform the data set to have years as the rows and countries as the columns
income = pd.read_excel("indicator gapminder gdp_per_capita_ppp.xlsx", index_col = 0).transpose()

#show the head of this data set when it is loaded
income.head()

#user interaction
while True:
    
    user_input = input("please enter a year between 1800 to 2012, or enter 'finish' to quit the program \n")
    
    if user_input == "finish":
        sys.exit()
    else:
        try:
            input_year = int(user_input)
            if len(user_input) == 4 and (input_year>=1800) and (input_year<=2012):
                income_distribution(input_year, income)
                break
            else:
                raise ValueError
            
        except ValueError:
            print("Invalid Input, please re-enter")

        except KeyboardInterrupt:
            sys.exit()
        except EOFError:
            sys.exit()

    

for year in range(2007, 2013):
    year_graphs = exploring_data_analysis(year)
    year_graphs.histogram_exploring()
    year_graphs.boxplot_exploring()
    
print("Finished, please open your dictionary to check those saved graphs")
    
