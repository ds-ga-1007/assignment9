import sys
from analysis_data import *

'''
Created on Dec 4, 2016

@author: sunyifu
'''

def main():
    
    countries, income = read_data()
    while True:
        try:
            year_input = input('Enter a year(type finish to quit):')
            if year_input.lower() == 'finish':
                for year in range(2007,2013):
                    merged_data =  merge_by_year(year, countries, income)
                    data = analysis_data(merged_data, year)
                    data.histogram()
                    data.boxplot()
                sys.exit()
            
            year = int(year_input)        
            if year not in income.index: 
                raise ValueError
            else:
                distribute_income(income,year)
                      
        except KeyboardInterrupt:
            sys.exit(0)      
        except EOFError:
            sys.exit(0)      

if __name__ == '__main__':
    main()