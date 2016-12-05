'''
world_Income_per_capita class
@author: jonathanatoy
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import matplotlib
import seaborn
from assignment9 import merge_by_year
class world_Income_per_capita(object):
    '''
    Class represents the income per capita for countries in the world in a given year
    '''


    def __init__(self, income, countries, year):
        '''
        Constructor for world_Income_per_capita class
        inputs:
                num_trials: An integer between 1800 and 2012 representing the year of interest
                
                
        
        '''
        import numpy as np
        self.income_data = merge_by_year(income, countries, year)
        self.year = year
        
        
    def income_dist_byRegion_box(self):
        '''
        Plots a boxplot of the income distribution across each region for the given year.
        output:
                PDF document named 'income_by_Region_<year>_box.pdf containing 6 boxplots 
                corresponding to the income per capita distribution in each region.
                
                
        
        '''
        fig = pl.figure(figsize = (15, 10))
        for i, region in enumerate(self.income_data['Region'].unique()):
            ax = fig.add_subplot(2, 3, i + 1)
            self.income_data[self.income_data.Region == region].plot(kind = 'box', ax = ax)
            pl.title(region, fontsize = 15)
            if i in [0,3]:
                pl.ylabel('Per Capita Income', fontsize = 18)
            else:
                pl.ylabel('')
        fig.suptitle('Distribution of Per Capita Income in ' + str(self.year), fontsize = 20)
        pl.savefig('income_by_Region_' + str(self.year) + '_box.pdf')
        
        
    def income_dist_byRegion_hist(self):
        '''
        Plots the histogram of the income distribution across each region for the given year.
        output:
                PDF document named 'income_by_Region_<year>_hist.pdf containing 6 histograms 
                corresponding to the income per capita distribution in each region.
                
                
        
        '''
        fig = pl.figure(figsize = (15, 10))
        for i, region in enumerate(self.income_data['Region'].unique()):
            ax = fig.add_subplot(2, 3, i + 1)
            self.income_data[self.income_data.Region == region].plot(kind = 'hist', ax = ax)
            pl.xticks(rotation = 30)
            pl.title(region, fontsize = 15)
            if i in [0,3]:
                pl.ylabel('Per Capita Income', fontsize = 18)
            else:
                pl.ylabel('')
        fig.suptitle('Distribution of Per Capita Income in ' + str(self.year), fontsize = 20)
        pl.savefig('income_by_Region_' + str(self.year) + '_hist.pdf')