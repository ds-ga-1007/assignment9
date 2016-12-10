"""
Created on Sat Dec 3 2016

@author: jinubak/jub205
@desc: This module consists of tool for GDP data analysis and graphical exploration.
"""
import sys
import pandas as pd
import matplotlib.pyplot as plt

def load_country_data(filename):
    '''This function loads the country data and return it as DataFrame'''
    
    try:
        countries = pd.read_csv(filename, dtype=str)
    except OSError:
        print("Invalid filename for country data")
        sys.exit(1)
    else:
        return countries
        
def load_gdp_data(filename):
    '''This function loads the GDP data, transforms it and returns it as DataFrame'''
    
    try:
        income = pd.read_excel(filename).T
        income.index = income.index.map(str)
    except:
        print("Invalid filename for GDP data")
        sys.exit(1)
    else:
        return income
    
def plot_income_distribution_by_year(data, year):
    '''This function takes Income/GDP data and year as arguments and
       plots the distribution of income per person across all countries
       for a given year.
    '''
    year_data = data.loc[year].dropna()
    plt.hist(year_data)
    plt.xlabel("Income per person")
    plt.ylabel("Frequency")
    plt.title("Histogram of income per person across the world")
    print("Please close the graph to continue with another year\n")
    plt.show()
    plt.close("all")
    
        
def merge_by_year(year, CountryData, IncomeData):
    '''This function takes country, income data and year as arguments and
       merges country and income data for a given year and returns a DataFrame
       with columns titled Country, Region, Income
    '''
    
    income_year_data = IncomeData.T[['gdp pc test',year]]
    income_year_data.columns = ['Country','Income']
    
    merged_data = CountryData.merge(income_year_data, on='Country', how='outer')
    merged_data = merged_data.dropna()
    merged_data['Income'] = merged_data['Income'].astype('float')
    
    return merged_data
    
def get_user_input():
    '''This function handles user input for year and checks the validity
       and returns if valid. Will ask user for input if invalid.
    '''
    
    valid_input = [str(i) for i in range(1800,2013)]
    valid_input.append('finish')
    
    ExitLoop = False
    
    while not ExitLoop:
        
        year = input("Please enter the year you are interested in[1800,2012]: ")
        year = year.strip().lower() #Clean up empty spaces and makes it lower case for comparison
        
        if year in valid_input:
            ExitLoop = True
        else:
            print("Invalid Year input")

    return year
    
class IncomeAnalysis:
    '''This class takes income data and year as arguments and graphically
       explores the distribution of the income per person by region data
    '''

    def __init__(self, IncomeData, year):
        
        self.data = IncomeData
        self.year = year
        
    def plot_boxplot(self):
        '''This function plots boxplot of the income per person by region
           and saves it as pdf file
        '''
        
        income_boxplot = self.data.boxplot(column="Income",by="Region")
        fig = income_boxplot.get_figure()
        fig.savefig("Box Plot of Income by region in %s.pdf"%self.year)
    
    def plot_histogram(self):
        '''This function plots histogram of the income per person by region
           and saves the plot as pdf file
        '''
        
        plt.close('all')
        hist_data = self.data.groupby('Region').Income.apply(list)
        plt.hist(list(hist_data.values), label = list(hist_data.index))
        plt.legend(loc=1)
        plt.xlabel("Income per person")
        plt.ylabel("Frequency")
        plt.title("Histogram of income per person by region in %s"%self.year)
        plt.savefig("Histogram of Income by region in %s.pdf"%self.year)
