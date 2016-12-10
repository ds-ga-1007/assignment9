"""
This program is to display the plot in question4 which is the distribution of income 
per person across all countries in the world for the given year, and save a histograms
and a boxplot grouped by region in question6 as pdf files.

User should type the year between 1800 - 2012, or 'finish' to quit the program. 

Xinyan Yang
NetID xy975
"""
import sys
from pac.functions import *
from pac.exploratory import *

def main():
    print('The program will display plots for a given year.')
    while True:
        input_p = input('Please input a year in 1800-2012 or finish to quit.')
        if input_p  == 'finish':
            sys.exit(0)
        else:
            try:
                year = year_valid(int(input_p))
                
                merge = merge_by_year(income, countries, year)
                print('exploratory plots saved.')
                print('close the all countries distribution plot to enter another year.')
                exploratory(merge,year).histograms()
                exploratory(merge,year).boxplot()
                ppp(income, year)
                
            except ValueError:
                print('Invalid input.')
   
if __name__ == "__main__":
    main()