# Solution for DS-GA 1007 Assignment#9
# Author: Yanan Shi y2506 N11812897

#from investiment import InvestmentInstrument
from exceptions import InvalidInputException
import matplotlib.pyplot as plt
import pandas as pd
from dataAnalysis import DataAnalysis
import sys


#check wether the input years is valid
def validYears(input):
    if not all(e.isdigit() for e in input):
        raise InvalidInputException
    years = int(input)
    if years not in range(1800, 2012 + 1):
        raise InvalidInputException
    return years



def main():
    #Load the countries.csv file (located in the assignment9 repository) into a pandas DataFrame and name this data set countries.
    countries = pd.read_csv('../countries.csv', index_col = 0)
    #Load the indicator gapminder gdp_per_capita_ppp.xlsx data set (located in the assignment9 repository) into a DataFrame called income.
    income = pd.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx',index_col=0)
    #The program should transform the data set to have years as the rows and countries as the columns, then show the head of this data set when it is loaded.
    incomeTrans = income.transpose()
    print("show the head of this data set when it is loaded:\n")
    print(incomeTrans.head())
    print("has showed the head of this data set:\n")
    #build a class object
    incomeData = DataAnalysis(income, countries)
    
    #The program should ask the user to enter a year, then display the graph using the function in question 4. Continue asking the user for a year and displaying the graph until the string ‘finish’ is entered.
    while True:
        try:
            #ask the user to enter a year
            inp = input("Input a year please, enter 'finish' to quit\n")
            if inp == 'finish':
                break
            years = validYears(inp)
            #graphically display the distribution of income per person across all countries in the world for the given year
            incomeData.distribution_income(years)
        #Invalid user input is handled correctly (when input is required by the assignment)
        #User defined exception(s) are employed for indicating error conditions rather than raising generic exceptions
        except InvalidInputException:
            # Exit if the user enter invalid input
            print("Invalid input")
        #sys.exit(0)
        except KeyboardInterrupt:
            # Exit if the user enter Ctrl+C
            sys.exit(0)
            print("Quited  by user")
        except EOFError:
            # Exit if the user enter Ctrl+D
            print("Quited  by user")
            sys.exit(0)
        except:
            print('exception happens')
    
    #use the class from question 6 to generate graphs for the years 2007-2012
    for year in range(2007, 2013):
        incomeData.generate_graphs(year)





if __name__ == "__main__":
    main()
