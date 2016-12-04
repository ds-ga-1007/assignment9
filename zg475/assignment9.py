'''
Main module for the program.
Enter a year, the program will display the distribution of income per person across all countries 
in the world for the given year until user prompts 'finish'.
The program will also generate histogram and boxplotgraphs for the years 2007-2012.

Created on Dec 3, 2016
@author: Zhiqi Guo(zg475)
@email: zg475@nyu.edu
'''
import sys
from graph import plot_income
from data_tool import dataTool
def main():
    while True:
        try:
            year = input('Please enter the year: ')
            if year == 'finish':
                print('END')
                sys.exit(0)
            try:
                year = int(year)
                if year < 1800 or year > 2012:
                    raise ValueError
                plot_income(year)
                
                for yr in range(2007,2013):
                    dataTool(yr).boxplot()
                    dataTool(yr).histogram()
                
            except ValueError:
                print('Invalid input!')
               
            
        except ValueError:
            print('Invalid input!')
        except KeyboardInterrupt:
            sys.exit(0)
            print('END')


if __name__ == '__main__':
    print('Keep entering year to get plot of distribution of income across all countries. ')
    print('Year starts from 1800 and end to 2012. ')
    print("Hint: enter 'finish' to interrupt program.")
    main()