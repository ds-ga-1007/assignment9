# Author: Leslie Huang (lh1036)
# Description: IncomeDistribution constructor and methods

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class IncomeDistribution(object):
    
    def __init__(self, this_year):
        self.this_year = this_year
    
    def compare_within_region(self):
        '''
        Generates one bar graph comparing income/pc by country within a region
        '''
        
        by_region = self.this_year.groupby("Region")
        
        for region in by_region.groups.keys():            
            current_region = by_region.get_group(region) # dataframe for the region
    
            region_plot = current_region.plot(kind = "bar", title = "Income/PC in Region: {}".format(region))
            plt.xlabel("Country")
            plt.ylabel("Income")
            
            # fix display issues: x-axis labels and title were crowded and cut off
            region_plot.set_xticklabels(current_region["Country"], size = 8)            
            plt.subplots_adjust(bottom = 0.5)

            plt.savefig("income_by_country_{}.pdf".format(region))
            plt.close()
    
    def compare_across_regions(self):
        '''
        Generates comparison boxplot of spread of average income/pc in each region
        '''
        pass
    
    def hist_within_region(self, bins = 10):
        '''
        Generates histogram for each region representing distribution of incomes across specified number of bins
        '''
        by_region = self.this_year.groupby("Region")
        
        for region in by_region.groups.keys():            
            current_region = by_region.get_group(region) # dataframe for the region
            
            region_plot = current_region.plot.hist(bins = bins, title = "Distribution of Income in Region: {}".format(region), grid = True)
            plt.xlabel("Income Ranges")
            plt.ylabel("Number of Countries that Fall in Income Range")
            plt.savefig("histogram_income_by_country_{}.pdf".format(region))
            plt.close()
        

# Sources consulted:
# http://pandas.pydata.org/pandas-docs/stable/groupby.html
# http://matplotlib.org/devdocs/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html
# http://matplotlib.org/faq/howto_faq.html#howto-subplots-adjust