'''
Created on 2016年12月4日

@author: bz866
'''

import matplotlib.pyplot as plt
import pandas as pd

class data_analysis:

    def __init__(self, merged_data, year):
        self.merged_data = merged_data
        self.year = year
        
    def histogram(self):
        """
        draw histogram 
        """
        year_number = self.year
        region_gdp = self.merged_data.groupby('Region').Income.apply(list)
        region_label = region_gdp.index.tolist()
        plt.hist(region_gdp, label=region_label)
        plt.legend(loc = 'best')
        plt.title("Histogram of distribution of people income by region in " + str(year_number))
        plt.xlabel('Income per person')
        plt.ylabel('')
        plt.savefig('Histogram of income in ' + str(year_number))
        plt.close()

    def boxplot(self):
        """
        draw boxplots
        """
        year_number = self.year
        self.merged_data.boxplot('Income', by = 'Region')
        plt.title("Boxplot of distribution of people income by region in " + str(year_number))
        plt.xlabel('Continent')
        plt.ylabel('Income per person')
        plt.savefig('Boxplot of income in ' + str(year_number))
        plt.close() 