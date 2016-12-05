import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from analysis import *

#Provide a main function that the user can input a year to get plots.
#When the user input a year from 1800 to 2012, it plot a histogram of income per capita in different countries.
#When the user input "finish", the it plots histograms and boxplots of income per capica in different regions from 2007 to 2012.
#When the user input a year is not between 1800 to 2012, then it raise inputerror. 
def main():
    countries = pd.read_csv("C:/Users/sherryyang/assignment9/countries.csv")
    income =pd.read_csv("C:/Users/sherryyang/assignment9/indicator gapminder gdp_per_capita_ppp.csv",index_col =0)
    income = income.T
    print(income.head())
    while True:
        try:
            user_input =str(input("Please input a year between 1800 and 2012:"))
            if user_input.lower() == "finish":
                for i in list(range(2007, 2013)):
                    merged =analysis.merge_by_year(income, countries, i)
                    analysis.income_by_region(income, countries, i)
                print('Finished')
                break
            
                
            if int(user_input)<1800 or int(user_input)>2012:
                raise InvalidInput("The year you input is out of range! Please input a year between 1800 and 2012.")
            analysis.income_by_countries(income,int(user_input))
        except InputError:
            print("Invalid positions input! It's not a year!")
        except KeyboardInterrupt:
            print("keyboard interrupt error")
        except EOFError:
            print("Value error")

if __name__ =="__main__":
    main()
    
class InputError(Exception):
    pass          

      
