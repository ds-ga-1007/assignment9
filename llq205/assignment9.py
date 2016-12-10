import pandas as pd
from graphs import *

"""Author: Li Lin Qin
main program to run by user, input 'finish' to quit program

When input a year between 1800 and 2012, 
this program will display the distribution of 
income per person across all countries in the world for the given year
"""
        
if __name__ == "__main__":
    countries = pd.read_csv("countries.csv")
    income = pd.read_excel("indicator gapminder gdp_per_capita_ppp.xlsx", index_col = 0)
    income = income.T
    #Print head of income dataset when loaded
    print(income.head())
    
    while True:
        year = input("Enter a year between 1800 and 2012 to display graphs: ")
        try:
            if year.lower() == 'finish':
                #if user input 'finish', generate graphs for the years 2007-2012 
                for y in range(2007, 2013):
                    merge = merge_by_year(countries, income, y)
                    plots = graphs.plotting(countries, income, y)
                print("Done!")
                break
            year = int(year)
            if year < 1800 or year > 2012:
                raise ValueError("Please input year between 1800 and 2012. ")
            income_per_person(income, year)
            
        except AttributeError:
            pass
        except ValueError:
            print("Invalid year. Please input an integer between 1800 and 2012. ")

