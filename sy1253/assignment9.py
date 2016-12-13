"""
Created on Mon Dec  5 01:37:07 2016

@author: Shucheng Yan
net ID: sy1253

credit wz1070 for data structure insight and unitest
"""

import pandas as pd
import matplotlib.pyplot as plt
import sys
from dataAnalysis import *
from summaryInfo import *

def main():
     countries = pd.read_csv('countries.csv')
     income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx', index_col = 0).transpose()
     print(income.head())
     
     while True:
         try:
             input_year = input("please enter a year between 1800 and 2012 to see income distribution: ")
             if input_year == 'finish':
                  for year in range(2007, 2013):
                      merged_data = mergeByYear(year, income, countries)
                      # create an obeject for each year
                      mergedPresent = dataAnalysis(year)
                      #present each year's histogram and boxplot
                      mergedPresent.histogram(merged_data)
                      mergedPresent.boxplot(merged_data)               
                  break
              
             elif int(input_year) >= 1800 and int(input_year) <= 2012:
                  inputYear = int(input_year)
                  displaySummary(inputYear, income)
                  
         except InputValueException:
            print("please enter a valid integer year between 1800 and 2012")                        
         except KeyboardInterrupt:
             sys.exit()
         except EOFError:
             sys.exit()


if __name__ == "__main__":
    main()
             
             