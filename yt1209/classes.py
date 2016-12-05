'''
Created on Dec 5, 2016

@author: Yovela
'''

import pandas as pd
import matplotlib.pyplot as plt
from functions import *


class exploring_data_analysis():
    
    '''
    Exploratory data analysis tools (histograms and boxplots) 
    Graphically explore the distribution of the income per person by region data set for a given year
    Save these graphs to individual files.

    '''


    def __init__(self, year):
        '''
        The data is merged income data set created by merged_by_year function and a given year
        '''
        self.year = year
        self.data = merge_by_year(year)
        
        
    def histogram_exploring(self):
        '''
        explore the distribution of the income per person by region data with histograms
        '''
        region_list = self.data.Region.unique()
        fig, axis = plt.subplots(nrows = 2, ncols = 3, figsize = (20,10))
        fig.suptitle = ("Histogram in region for" + str(self.year))
        i,j = 0,0
        for region in region_list[0:3]:
            data_region = self.data[self.data['Region'] == region][["Country", "Income"]]
            data_region.hist(ax = axis[i,j])
            axis[i,j].set_title("Histograms for Income in "+region)
            j = j+1
        i,j = 1,0
        for region in region_list[3:6]:
            data_region = self.data[self.data['Region'] == region][["Country", "Income"]]
            data_region.hist(ax = axis[i,j])
            axis[i,j].set_title("Histograms for Income in "+region)
            j = j+1
        
        plt.savefig("Histograms for Income in " + str(self.year))         
        return
            
    def boxplot_exploring(self):
        '''
        explore the distribution of the income per person by region data with boxplots
        '''
        self.data.boxplot(by = "Region")
        plt.savefig("Boxplots for income in different regions in" + str(self.year))
        return
    
