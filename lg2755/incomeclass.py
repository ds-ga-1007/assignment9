'''
Author: lg2755
Date: Dec 03, 2016
DS_1007 Assignment 9

This is the main program for assignment 9.
'''

import pandas as pd
import matplotlib.pyplot as plt

def displayIncomeDistribution(year, income):
    '''
        This function generates a histogram that displays of the distribution of income per person across all countries in the world for a given year.
        '''
    oneyear = income.loc[year, :].copy()
    plt.hist(oneyear.dropna())
    plt.xlabel('Income per capita')
    plt.ylabel('Number of countries')
    plt.title('Distribution of Income Per Capita Across Countries')
    plt.show()

def mergeByYear(year, income, countries):
    '''
        This function merges the two data frames, "countries" and "income" by any given year. The function generates a merged data frame.
        '''
    merged_dataframe = pd.merge(countries, income.loc[year,:].to_frame('Income'), left_on='Country', right_index=True)
    return merged_dataframe

class ExploreDistribution(object):
    '''
        This class includes two methods. One generates a histogram to display the income per capita by country within a region. The other generates a boxplot for a region.
        '''
    def __init__(self, data):
        self.data = data
    
    def generateHistogram(self):
        for region in self.data.Region.unique():
            income_regional = self.data[self.data['Region'] == region]['Income'].dropna()
            plt.hist(income_regional.values, color = 'orange', alpha = 0.8)
            plt.title('Income Per Capita Distribution Histogram For %s'%region)
            plt.show()
    
    def generateBoxplots(self):
        for region in self.data.Region.unique():
            income_regional = self.data[self.data['Region'] == region]['Income'].dropna()
            plt.boxplot(income_regional.values)
            plt.title('Income Per Capita Distribution Boxplot For %s'%region)
            plt.show()

class InputValueException(Exception):
    '''
        Define an exception class
        '''
    pass