# Author: Leslie Huang (lh1036)
# Description: IncomeDistribution constructor and methods

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class IncomeDistribution(object):
    
    def __init__(self, data, year):
        self.data = data
        self.year = year
    
    def compare_within_region(self):
        '''
        Generates one bar graph comparing income/pc by country within a region
        '''
        
        by_region = self.data.groupby("Region")
        
        for region in by_region.groups.keys():            
            current_region = by_region.get_group(region) # dataframe for the region
    
            region_plot = current_region.plot(kind = "bar", title = "Income/PC in Region: {}, {}".format(region, self.year))
            plt.xlabel("Country")
            plt.ylabel("Income")
            
            # fix display issues: x-axis labels and title were crowded and cut off
            region_plot.set_xticklabels(current_region["Country"], size = 8)            
            plt.subplots_adjust(bottom = 0.5)

            plt.savefig("{}_income_by_country_{}.pdf".format(self.year, region))
            plt.close()
    
    def compare_regional_income_spread(self):
        '''
        Generates comparison boxplot of spread of average income/pc in each region
        '''
        
        comparison_plot = self.data.boxplot(by = "Region", return_type = "dict", rot = 90)
        plt.xlabel("Region")
        plt.subplots_adjust(bottom = 0.3)
    
        # add title and get rid of automatically added title
        plt.title("Spread of Income PC, Grouped by Region {}".format(self.year))
        plt.suptitle("")
        
        plt.savefig("{}_regional_spread_income.pdf".format(self.year))
        plt.close()
    
    def hist_within_region(self, bins = 10):
        '''
        Generates histogram for each region representing distribution of incomes across specified number of bins
        '''
        
        by_region = self.data.groupby("Region")
        
        # calculate values to use as xlim and ylim in plot based on bounds of the data
        max_income = self.data["Income"].max()
        max_region_count = max([len(by_region.get_group(region)) for region in by_region.groups.keys()]) / (bins / 2)
        
        for region in by_region.groups.keys():            
            current_region = by_region.get_group(region) # dataframe for the region
            
            region_plot = current_region.plot.hist(bins = bins, title = "Distribution of Income in Region: {}, {}".format(region, self.year), grid = True)
            
            plt.xlabel("Income Ranges")
            plt.ylabel("Number of Countries that Fall in Income Range")
            
            axes = plt.gca()
            axes.set_xlim([0, max_income])
            axes.set_ylim([0, max_region_count])
            
            plt.savefig("{}_hist_income_by_country_{}.pdf".format(self.year, region))
            plt.close()
        

# Sources consulted:
# http://pandas.pydata.org/pandas-docs/stable/groupby.html
# http://matplotlib.org/devdocs/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html
# http://matplotlib.org/faq/howto_faq.html#howto-subplots-adjust