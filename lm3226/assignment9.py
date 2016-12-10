"""
Date: Dec 5, 2016
Author: Chloe Meng(lm3226)
Description: This program asks user to provide a year that they would like to see the GDP per capita.
"""

from read_and_display_GDP import *
from data_analysis_graphs import *
import sys

def main():
    while True:
        try:
            user_input_year = input('Please enter a year between 1800 and 2012: ')
            if user_input_year == 'finish':
                sys.exit(0)
            try:
                user_year = int(user_input_year)
                if user_year < 1800 or user_year > 2012:
                    raise ValueError
                year = read_and_display_GDP(user_year)
                year.generate_income_barchart()

                for i in range(2007,2013):
                    example_year = data_analysis_graphs(i)
                    example_year.generate_merged_income_histogram()
                    example_year.generate_merged_income_boxplot()
            except ValueError:
                print('Invalid input. Please try again: ')

        except ValueError:
            print('Invalid input. Please try again:')
        except KeyboardInterrupt:
            sys.exit(0)

if __name__ == '__main__':
    print("This program asks to input a year in order to provide user a bar chart for countries' GDP per capita for the given year.")
    print('This program will also provide histogams and boxplots of GDP per capita that merged by regions between 2007 to 2012.')
    print("If you would like to quit, please enter 'finish'. ")
    main()
