import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from analysis import *

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

      
