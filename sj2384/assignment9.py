'''
Created on Dec 5, 2016

@author: sj238
'''
from dataNmerge import *
from dataNtools import *
import sys

def main():
    """
    The main function ask the user to input a year, then display income per person distribution
    of each country for a given year using vertical bar plot by calling the function
    incomeDistribution. Continue asking the user for a year and displaying the distribution 
    until the 'finish' is entered to quit and get graphs for the years 2007-2012.
    """
    print(income.head())

    while True:
        try:
            input_year = input("Please enter the year between 1800 and 2012, or 'finish'to quit: ")
            if input_year == 'finish':
                for i in range(2007, 2013):
                    data =  merge_by_year(i)
                    graph = graphs(data, i)
                    graph.histogram()
                    graph.boxplot()
                sys.exit()
            if int(input_year) in list(income.index[:]):
                incomeDistribution(int(input_year))
            else: 
                raise ValueError
        except KeyboardInterrupt:
            sys.exit()
        except EOFError:
            sys.exit()   
                

if __name__ == '__main__':
    main()