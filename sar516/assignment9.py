import pandas as pd
import numpy as np
from Income import Yearly_Income


countries = pd.read_csv("../countries.csv", index_col = 0)
income = pd.read_excel("../indicator gapminder gdp_per_capita_ppp.xlsx", index_col = 0)

countries = countries.transpose()
income = income.transpose()

def merge_by_year(countries, income, year) :
    """This function will merge the income and countries dataframe for  single year"""
    # Here the function finds the common countries between the two dataframes and sets
    # up the empty dictionary that will be turned into the output dataframe
    common = np.intersect1d(countries.columns.values, income.columns.values)
    data_dict = {"Country" : [], "Region" : [], "Income" : []}
    
    # Here the function goes through each country and fills in the appropriate values
    for country in common :
        data_dict["Country"].append(country)
        data_dict["Region"].append(countries[country]["Region"])
        
        #Here Thee function sets NaN values to zero
        if str(income[country][year]) == "nan" :
            data_dict["Income"].append(0)
        else: 
            data_dict["Income"].append(income[country][year])
    else:
        return pd.DataFrame(data_dict)
    
def yearly_histo(countries, income, year) :
    """This function creates a histogram that will show the distribution of income
       across all countries"""
    import matplotlib.pyplot as plt
    
    data = merge_by_year(countries, income, year)
    
    plt.hist(data["Income"], bins = 30)
    plt.xlabel("Income per person")
    plt.ylabel("Number of Countries")
    plt.title("Histogram of Income per person for the year " + str(year))
    plt.show()
    
def ask_year():
    """This function simply asks the user for the year they want to look at"""
    year_input = input("Please enter the year you wish to look at" + "\n")
    if year_input == "finish" :
        return year_input
    else:
        return int(year_input)
    
def get_user_input():
    """This function keeps asking the user for a year until they type 'finish'."""
    not_quit = True
    while not_quit :
        is_number = False
    
        # Here the program checks to see if a number was entered
        try:
            year = ask_year()
        except ValueError:
            print("What you have entered is not a year. If you wich to quit the program please type 'finish'.")
        else :
            is_number = True
    
        # Here the program make sure a proper year was entered orchecks if the 
        # user wants to quit
        if is_number :
            if year in range(1800, 2013) :
                yearly_histo(countries, income, year)
            elif year == "finish":
                not_quit = False
            else:
                print("The number you have entered is not a valid year. Please enter a year between 1800 and 2012.")

if __name__ == '__main__':                
    in_loop = True                
    while in_loop :
        try:
            for years in range(2007, 2013):
                data = merge_by_year(countries, income, years)
                info = Yearly_Income(data, years)
                info.regional_boxplot("Graphs")
                info.regional_histos("Graphs")
            get_user_input()
        except KeyboardInterrupt:
            Print("please type 'finish' if you wish to quit the program")
        else:
            in_loop = False
    