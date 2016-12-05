import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from distribution_year import *
from data_analysis_tools import *
from merge_year import *
import sys

"""
Author: Wenjie Sun
"""

# load data frame countries
countries = pd.read_csv("countries.csv")
# load income, reset the index column to gdp pc test for next step
income = pd.read_excel("indicator gapminder gdp_per_capita_ppp.xlsx",sheetname="Data",index_col = "gdp pc test")
# swap the column and row
income = income.T

# generate a list of all years. This will be used in the following function to validate if the input is with in the year range
year_list = list(income.index)

#Q3 - generate the income.head as well as save into the folder 
income_head = income.head()
print(income_head)
income_head.to_csv("Q3 - Income Head.csv")

#Q4
# This block handles all the situation that input is not in the range, input is not an integer, and the correct input
# use pre-defined the class to plot. Details are in distribution_year class
while True:
    try:
        input_year = input("Which year do you want to plot of income per person? Or type finish: ")
        if input_year.upper() == str("FINISH"):
            break
        try:
            int_input_year = int(input_year)
            if int_input_year not in year_list:
                print ("Input is not in the range")
                continue
            plot_distribution_year = distribution_year(income, input_year)
            plot_distribution_year.plot()
        except ValueError:

            print ("Input is not an integer")
            continue
    except ValueError:
        print ("Error")
        continue
    except KeyboardInterrupt:
        sys.exit(0)
    except EOFError:
        sys.exit(0)


#Q6
# without asking, the program will continue run the boxplot and histogram plot for the requested year
# use pre-define the merge_year class to handle the merged year function
year_generate = [2007,2008,2009,2010,2011,2012]

for int_input_year in year_generate:
    analysis_year_merged_data = merge_year(income, countries, int_input_year)
    data_analysis = data_analysis_tools(analysis_year_merged_data.result(), int_input_year)
    data_analysis.plot()

# almost the same as the pervious block, the block handles input and use pre-define data_analysis_tools class
# details are in the data_analysis_tools class
while True:
    try:
        input_year = input("Any other year want to explore? Or type finish: ")
        if input_year.upper() == str("FINISH"):
            break
        try:
            int_input_year = int(input_year)
            if int_input_year not in year_list:
                print ("Input is not in the range")
                continue
            analysis_year_merged_data = merge_year(income, countries, int_input_year)
            data_analysis = data_analysis_tools(analysis_year_merged_data.result(),int_input_year)
            data_analysis.plot()
        except ValueError:
            print ("Input is not an integer")
            continue
    except ValueError:
        print ("Error")
        continue
    except KeyboardInterrupt:
        sys.exit(0)
    except EOFError:
        sys.exit(0)




