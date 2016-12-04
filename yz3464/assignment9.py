'''
Created on Dec 3, 2016

@author: twff
'''
import sys
from tools import *

if __name__=='__main__':
    countries = pd.read_csv('/Users/twff/assignment9/yz3464/countries.csv', index_col = 0) #question1
    income = pd.read_excel('/Users/twff/assignment9/yz3464/indicator gapminder gdp_per_capita_ppp.xlsx',index_col = 0)#question2
    income_transpose = income.T
    print(income_transpose.head())#question 3
    
    try:
        user_input = input('Input year or enter finish: ')
        #show income distribution plot
        while user_input != 'finish':#question7
            try:
                year = int(user_input)
                incomeDistribution(income, year)
            except ValueError:
                print('Invalid input')
            user_input = input('Input year or enter finish: ')
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(1)
        
    tool = tools()   #question8
    for year in range(2007,2013):
        merged = merge_by_year(countries, income, year)
        tool.boxplot_by_region(merged, 'boxplot %d.pdf' %year, year)
        tool.histogram_by_region(merged, 'histogram %d.pdf' %year, year)
    
    print('Finish plot')
    
        
        