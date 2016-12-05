from Data_processing import *
import matplotlib.pyplot as plt
import pandas as pd
'''
Created on Dec 3, 2016
@author: Yanli Zhou
'''
class Data_tool(object):
    '''
    This class uses data analysis tools (histograms and boxplots) to explore visually the distribution
    of income per person by region for a given year.
    '''
    def __init__(self, year):
        '''
        Constructor of object Data_tool
        '''
        self.year = year
        self.data = merge_by_year(year)
        
    def histogram(self):  
        '''
        Histogram of income across all countries of given year
        '''
        plt.subplots(figsize=(10,10)) 
        self.data['Income'].dropna().hist()
        thistitle = 'Histogram of income of year '+str(self.year)
        plt.title(thistitle)
        plt.xlabel('Income per person')
        plt.ylabel('Count')
        plt.ylim(0,120)
        plt.xlim(0,100000)
        plt.savefig(thistitle+'.pdf')

        
    def boxplot(self):
        '''
        Boxplot of income across all regions of given year
        '''
        plt.subplots(figsize=(10,10)) 
        self.data['Income'] = self.data['Income'].astype(float)
        self.data.boxplot('Income',by='Region')
        thistitle = 'Boxplot of income across regions of year '+str(self.year)
        plt.ylim(0,100000)
        plt.savefig(thistitle+'.pdf')
