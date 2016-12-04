'''
Created on Dec 3, 2016
@author: Zhiqi Guo(zg475)
@email: zg475@nyu.edu
'''
from graph import merge_by_year, plot_income
import matplotlib.pyplot as plt
import pandas as pd

class dataTool(object):
    '''
    uses data analysis tools (histograms and boxplots) to graphically explore the distribution
    of the income per person by region dataset for a given year.
    '''
    def __init__(self, year):
        '''
        Constructor
        '''
        self.year = year
        self.df = merge_by_year(year)
        
    def histogram(self):  
        '''
        Histogram for Income across all countries at a specific given year
        '''
        fig, ax = plt.subplots(figsize=(10,10)) 
        self.df['Income'].dropna().hist()
        ax.set_title('Histogram of income for year '+str(self.year))
        ax.set_xlabel('Income per person')
        ax.set_ylabel('Count')
        fig.savefig('Distribution of income '+str(self.year)+'.pdf')
    
    def boxplot(self):
        '''
        Boxplot for Income at a specific given year, groupby by Region
        '''
        fig, ax = plt.subplots(figsize=(10,10)) 
        self.df['Income'] = self.df['Income'].astype(float)
        self.df.boxplot('Income',by='Region',ax=ax)
        fig.savefig('Boxplot of income for regions for year '+str(self.year)+'.pdf')
