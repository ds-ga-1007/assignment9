'''
Created on Dec 4, 2016

@author: felix
'''

import pandas as pd
import matplotlib.pyplot as plt
import re

def valid_year_str(string):
    if re.match(r"^\d{4}$", string):
        # must be four digits
        return True
    else:
        return False

def valid_finish_str(string):
    if string.upper() == 'FINISH':
        return True
    else:
        return False
    
def valid_user_str(string):
    if valid_year_str(string) or valid_finish_str(string):
        return True
    else:
        return False

def get_countries(file_location = '../countries.csv'):
    # Question 1
    countries = pd.read_csv(file_location,  index_col=0)
    return countries

def get_income(file_location = '../indicator gapminder gdp_per_capita_ppp.xlsx'):
    # This function relies on pd.read_excel, which requires the package 'xlrd'
    # Question 2
    income = pd.read_excel(file_location, index_col=0) 
    return income

class InvalidYearException(Exception):
    pass

class Income:
    '''
    Creates a class based on countries data and income data
    
    '''
    def __init__(self, countries_data, income_data):
        self.countries = countries_data
        self.income = income_data
        self.income_transposed = self.income.transpose()
        
    def year_is_valid(self, year):
        #print(self.income.index)
        if year in self.income_transposed.index:
            return True
        else:
            return False
        
    def plot_distribution_of_year(self, year):
        # Question 4
        if self.year_is_valid(year):
            this_year_income = self.income_transposed.ix[year].dropna() # only use the data of the entered year, excluding NaNs
            fig = plt.figure()
            plt.hist(this_year_income, bins = 25)
            this_title = 'Distribution of Income per Person across All Countries for ' + str(year)
            plt.title(this_title)
            plt.xlabel('Income ($)')
            plt.ylabel('Number of Countries')
            plt.savefig('./Plots/'+this_title+'.pdf')
            plt.show()
            plt.close()
        else:
            raise InvalidYearException('Year input not valid')
            
    def merge_by_year(self, year):
        # Question 5
        if self.year_is_valid(year):
            this_year_income = pd.DataFrame(self.income[year])
            merged_data = pd.merge(self.countries, this_year_income, left_index = True, right_index = True)
            merged_data["Country"] = merged_data.index
            merged_data.rename(columns = {year:'Income'}, inplace = True)
            merged_data = merged_data[['Country','Region','Income']] # Order the columns as required
            return merged_data
        else:
            raise InvalidYearException('Year input not valid')