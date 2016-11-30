""" Question 1 to 5 which are functions will be used to run the main program """

import pandas as pd
import matplotlib.pyplot as plt
import os


# import os to get the working directory
# in my case, the working path is usually '.../assignment9/yz2777'
path = os.getcwd()

# I try to let the program can load the data automatically
# since countries.csv and  indicator gapminder gdp_per_capita_ppp.xlsx are located in 'assignment9' folder
# we remove the netID yz2777 and make path for "countries" and "indicator"
file_path = path[:-6]

# path for countries.csv
file_path_c = file_path + 'countries.csv'

# path for indicator gapminder gdp_per_capita_ppp.xlsx
file_path_i = file_path + 'indicator gapminder gdp_per_capita_ppp.xlsx'


# Q1
# define a function to load countries.csv and named as "countries"
def read_countries(file):
    countries = pd.read_csv(file)
    return countries

# Q2 and Q3
# define a function to load indicator gapminder gdp_per_capita_ppp.xlsx and named as "income"
# transpose the rows and columns
# show the head of the data when loaded
def read_income(file):
    income = pd.read_excel(file,sheetname='Data',index_col = 0)
    income_trans = income.transpose()  # refer to online pandas 0.19.1 documentation
    print (income_trans.head())
    return income_trans

# Q4
# plot histogram to dsiplay the distribution of income per person across all countries in the world for the given year
def plot_income_by_year(year,income_file):
    income_by_year = income_file.ix[year]  # given a year and get the income for all countries
    income_by_year.hist(bins=100)
    plt.xlabel('income per person')
    plt.ylabel('count')
    plt.title('histogram of income per person across all countries in the world for the year {0}'.format(year))
    plt.grid(True)
    plt.show()
    
# Q5
# merge data by countries
def merge_by_year(year):
    # load the data, the path should not need to change, but need to make sure
    countries = read_countries(file_path_c)            # load "countries.csv"
    income = read_income(file_path_i)                  # load "indicator gapminder gdp_per_capita_ppp.xlsx"
    new_income_year = income.ix[[year]].transpose()    # transpose the row and col
    # rename col to 'Income' and create a col called 'Country' based on index
    new_income_year.columns = ['Income']
    new_income_year['Country'] = new_income_year.index
    # merge data by 'Country' and the method is "left" which means that focus on the countries from "countries.csv"
    merge_data = pd.merge(countries,new_income_year,on='Country',how='left')
    return merge_data
