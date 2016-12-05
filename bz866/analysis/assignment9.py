'''
Created on 2016年12月4日

@author: bz866
'''

from analysis.data_analysis import *
from analysis.functions import *
import sys

def main():
    countries, income = read_data()
    
    while True:
        try:
            str_year = input('Input a year number between 1800 and 2012, or finish:\n' +
                            '(boxplot for 2007-2012 will be generated after all search ends)')
            
            '''boxplot for 2007-2012 will be generated after all search ends'''
            for i in range(2007, 2013):
                    merged_data =  merge_by_year(i, countries, income)
                    d = data_analysis(merged_data, i)
                    d.histogram()
                    d.boxplot()
                    
            if (str_year == 'finish'):
                sys.exit()
            
            year = int(str_year)

            if (1800 <= year and year <= 2012):
                show_distribution(income, year)
            else: 
                raise ValueError
        except ValueError:
            print('Invalid year number')
        except KeyboardInterrupt:
            sys.exit()
        except EOFError:
            sys.exit()

if __name__ == "__main__":
    main()  
