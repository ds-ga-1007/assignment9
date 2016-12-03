
import sys
import Position
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def graph_income(income, year):
    incomes_at_year = income.ix[year,:]
    incomes_at_year.hist()
    plt.show()
    


def merge_by_year(income, countries, year):
    if not isinstance(income, pd.DataFrame) or not isinstance(countries, pd.DataFrame):
        raise ValiueError("income and countries must be pandas DataFrames")
    try: 
        year = int(year)
    except ValueError:
        raise ValueError("year must be an integer")
    try:
        merged_df = countries.merge(income.transpose().ix[:,[year]], left_on = 'Country', right_index = True)
    except KeyError:
        raise KeyError("countries must have Country Column")
    merged_df.columns = ['Country', 'Region', 'income']
    merged_df.year = year

    return merged_df

class EconVisualizer(object):
    
    def __init__(self, income = None, countries = None):
        self.income = income
        self.countries = countries
    
    def graph_years(self, years):
        
        if not isinstance(years, list):
            raise ValueError("can only graph years where years is a list of integers")
            
        if not isinstance(self.income, pd.DataFrame) or not isinstance(self.countries, pd.DataFrame):
            raise ValueError("EconVisualizers must have pandas DataFrames for income and countries to graph lists of years")
        for year in years:
            try:
                year = int(year)
            except ValueError:
                raise ValueError("Every year in years to graph must be an integer")
            merged_df = merge_by_year(self.income, self.countries, year)
            ev.box(merged_df, visualize = False)
            ev.hist(merged_df, visualize = False)
            
    def hist(self, df, visualize = True):
        
        try:
            income = df['income']
        except KeyError:
            raise ValueError('econ visualizer histograms require income columns')
        plt.figure()
        income.hist()
        
        try:
            year_label = 'year ' + str(df.year)
        except AttributeError:
            year_label = 'an unknown year'
            
        plt.title("histograms of incomes from " + year_label)
        plt.xlabel('average income per person')
        plt.ylabel('percent of countries with average income in range')
        plt.savefig('histogram of incomes from ' + year_label + '.png')
        if visualize:
            plt.show()   
            
    def box(self, df, visualize = True):
        
        try:
            income = df[['income']]
        except KeyError:
            raise ValueError('econ visualizer booxplots require income columns')
        plt.figure()   
        income.boxplot()
        
        try:
            year_label = 'year ' + str(df.year)
        except AttributeError:
            year_label = 'an unknown year'
            
        plt.title("box plot of incomes from " + year_label)
        plt.ylabel('average income per person')
        plt.savefig('boxplot of incomes from ' + year_label + '.png')
        if visualize:
            plt.show()   


if __name__ == '__main__':
    """
    
    """
    try:
        countries = pd.read_csv('../countries.csv')
        income = pd.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx', index_col = 0).transpose()
    except FileNotFoundError:
        raise FileNotFoundError("countries.csv and indicator gapminder gdp_per_capita_ppp.xlsx need to be in the parent directory")
        
    while True:
        try:
            user_input = input("What year would you like to see? Finish to complete report, ctrl+c or ctrl+d to exit")
        except KeyboardInterrupt:
            # Exit if the user enters Ctrl+C
            sys.exit(0)
        except EOFError:
            # Exit if the user enters Ctrl+D
            sys.exit(0)
        if user_input.lower() == 'finish':
            break
        try:
            year = int(user_input)
        except ValueError:
            print("year must be an integer")
        else:
            # Raises a ValueError and loops back if user_input is not correctly structured
            # as a sequence of intervals
            merged_df = merge_by_year(income, countries, year)
        try:
            graph_income(income, year)
        except:
            print('year ' + str(year) + " not in range. Try again?")
    #Here out of the while loop, the user had to exit the while loop by typing Finish.
    #Now we generate graphs for the years 2007-2012.
    ev = EconVisualizer(income, countries)
    ev.graph_years(list(range(2007, 2013)))

            
            
            
            

