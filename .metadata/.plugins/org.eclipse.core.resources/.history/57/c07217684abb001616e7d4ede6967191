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
        This method use the merged_data to group by region, and then draw the histogram and save those graphs.
        """
        region_gdp = self.merged_data.groupby('Region').Income.apply(list)
        region_label = region_gdp.index.tolist()
        plt.hist(region_gdp, label=region_label)
        plt.legend(loc = 'best')
        plt.title("Histogram of distribution of the income per person by region in " + str(self.year))
        plt.xlabel('Income per person')
        plt.ylabel('')
        plt.savefig('Histogram of income in ' + str(self.year))
        plt.close()

    def boxplot(self):
        """
        This method use the merged_data to group by region, and then draw the boxplot and save those graphs.
        """
        self.merged_data.boxplot('Income', by = 'Region')
        plt.title("Boxplot of distribution of the income per person by region in " + str(self.year))
        plt.xlabel('Continent')
        plt.ylabel('Income per person')
        plt.savefig('Boxplot of income in ' + str(self.year))
        plt.close() 