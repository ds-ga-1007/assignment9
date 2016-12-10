import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

'''function that function to graphically display the distribution of income per person
across all countries in the world for the given year, taking income and year as inputs,
and returns a histogram plot.
'''
def income_distribution(income, year):
    plt.hist(income.loc[year].dropna())
    plt.xlabel('Income per person')
    plt.ylabel('Countries')
    plt.title('Distribution of income per person across all countries in the world')
    plt.show()
    plt.close()
    
'''function to merge the countries and income data sets for any given year,
taking year, contries and income as inputs, and returns a dataframe with
three columns titled Country, Region, and Income.
'''
def merge_by_year(year, countries, income):
    income_data = income.T[['gdp pc test',year]]
    income_data.columns = ['Country','Income']
    merged_data = countries.merge(income_data, on='Country', how='outer')
    merged_data = merged_data.dropna()
    merged_data['Income'] = merged_data['Income'].astype('float')
    return merged_data

'''Provide a class that uses exploratory data analysis tools (histograms and boxplots) 
to graphically explore the distribution of the income per person by region data set
from question 5 for a given year. Save these graphs to individual files.
'''

class analysis:
    def __init__(self, merged_df, year):
        self.merged_df = merged_df
        self.year      = year
        
    def hist_plot(self):
        hist_data = self.merged_df.groupby('Region').Income.apply(list)
        plt.hist(list(hist_data.values), label = list(hist_data.index))
        
        plt.xlabel('Income per person')
        plt.ylabel('Countries')
        plt.title('Histogram plot of income per person across regions')
        plt.savefig('Histogram of ' + str(self.year) +'.pdf')
        plt.close()
    
    def box_plot(self):
        
        self.merged_df['Income'] = list(self.merged_df['Income'])
        self.merged_df.boxplot(column = 'Income', by = 'Region')
        
        plt.xlabel('Region')
        plt.ylabel('Income per person')
        plt.title('Box plot of income per person across regions')
        plt.savefig('Boxplot of ' + str(self.year) +'.pdf')
        plt.close()
