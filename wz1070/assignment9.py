#@auther wz1070
# This program reads in an input of year from user and display the corresponding 
# distribution of GDP per person. If the input is finish, then it will plot the 
# histogram and boxplot from 2007 to 2012. 

import pandas as pd
from DataAnalysis import *
from Methods import *
from InvalidInputException import *
import sys

if __name__ == '__main__':
    countries = pd.read_csv('countries.csv')
    income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx', index_col = 0).T
    print(income.head())
    while(True):
        try:
            year_string = input('Enter a year between 1800 and 2012 to display the distribution, or \'finish\' to exit')
            if year_string.isdigit() and int(year_string) >= 1800 and int(year_string) <= 2012:
                year = int(year_string)
                displayIncome(year, income)
            elif year_string == 'finish':
                for i in range(2007, 2013):
                    cur_data = merge_by_year(i, income, countries)
                    cur_data_analysis = DataAnalysis(i)
                    cur_data_analysis.histogram(cur_data)
                    cur_data_analysis.boxplot(cur_data)
                break
            else:
                raise InvalidInputException()
        except KeyboardInterrupt:
            sys.exit()