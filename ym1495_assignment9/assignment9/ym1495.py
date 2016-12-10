'''
Created on Dec 5, 2016

@author: muriel820
'''
import pandas as pd
import sys
from assignment9.functions import *
from assignment9.loadData import *
from assignment9.functions import *
from assignment9.exceptions import *

def main():
    Dataframes = loadData()
    while True:
        try:
            year = input('Please enter a four digit year in the past or end with finish')
            if year.lower()=='finish':
                break
            else: 
                year = int(year)
                if year not in Dataframes.income.index:
                    raise invalid_input()
                else: 
                    #overall_income_distr(Dataframes.income,year)
                    continue
                continue
        except invalid_input:
            print("Invalid input, please try again")
            continue
        except ValueError as ex:
            print("It's not an integer, Please check your input, and type a four digit year, or end with finish")
            continue
        except KeyboardInterrupt:
            sys.exit(0)      
        except EOFError:
            sys.exit(0) 
            
        for year in range(2007,2013):
            merged_data =  merge_by_year(Dataframes.income, Dataframes.countries,year)
            data_to_plot = plotting_functions(merged_data, year)
            data_to_plot.histogram()
            data_to_plot.boxplot()
        sys.exit()
        
if __name__ == '__main__':
    main()