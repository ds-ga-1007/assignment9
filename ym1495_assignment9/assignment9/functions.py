'''
Created on Dec 5, 2016

@author: muriel820
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def overall_income_distr(income,year):
    plt.hist(income.loc[year].dropna())
    plt.xlabel('Income per person')
    plt.ylabel('Number of countries')
    plt.title('Distribution of income per person around the world in' + str(year))
    plt.show()
    plt.close()

def merge_by_year(income,countries,year):
     temp = pd.DataFrame(income.loc[year]).reset_index()
     temp = temp.rename(columns = {'gdp pc test':'Country'})
     temp = temp.rename(columns = {year:'Income'})
     merged_by_year = pd.merge(countries,temp,on='Country')
     return(merged_by_year)

class plotting_functions(object):
    '''
    define a class with boxplot and histogram
    '''
    def __init__(self,data,year):
        '''
        Constructor
        '''
        self.data = data
        self.year = year 
    
    def boxplot(self):
        self.data['Income'] = list(self.data['Income'])
        self.data.boxplot(column = 'Income', by = 'Region', figsize=(12,12))
        plt.title('Boxplot of income per person across regions')
        plt.ylabel('Income per person')
        plt.xlabel('Region')
        plt.savefig('Boxplot of year: ' +str(self.year) + '.pdf')
        plt.close()
        
    def histogram(self):
        region_wide_gdp = self.data.groupby('Region').Income.apply(list)
        region_label = region_wide_gdp.index.tolist()
        plt.hist(region_wide_gdp, label=region_label)
        plt.xlabel('Income per person')
        plt.ylabel('Number of countries')
        plt.title('Histogram of income per person across regions ' )
        plt.legend()
        plt.savefig('Histogram of year: ' + str(self.year) +'.pdf')
        plt.close()
