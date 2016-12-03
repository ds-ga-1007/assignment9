# Author: Leslie Huang (lh1036)
# Description: IncomeDistribution constructor and methods (Question 6)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from .exceptions import *

class IncomeDistribution(object):
    
    def __init__(self, data, year):
        '''
        Constructor
        '''
        self.data = data
        self.year = year
    
    def plot_world_income_for_year(self):
        '''
        Question 4: Return bar graph of each country's income/pc for a given year
        '''
        year_plot = self.data.plot(kind = "barh", title = "Income by Country in {}".format(self.year))
        year_plot.set_xlabel("Income")
        plt.show()
    
        return year_plot
    
    def compare_within_region(self):
        '''
        Question 6: Generates one bar graph per region
        Each bar graph compares income/pc by country in that region
        '''
        
        by_region = self.data.groupby("Region")
        
        ### generate graph for each region, label axes, and save file
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
        Question 6: Generates one boxplot representing the spread of income/pc for each region
        '''
        
        comparison_plot = self.data.boxplot(by = "Region", return_type = "dict", rot = 90)
        
        # Adjust x axis label and margins
        plt.xlabel("Region")
        plt.subplots_adjust(bottom = 0.3)
    
        # add title and get rid of automatically added title
        plt.title("Spread of Income PC, Grouped by Region {}".format(self.year))
        plt.suptitle("")
        
        # To allow for comparison of graphs from different years, manually set the ylim 
        axes = plt.gca()
        axes.set_ylim([0, 100000])
        
        plt.savefig("{}_regional_spread_income.pdf".format(self.year))
        plt.close()
    
    def hist_within_region(self, bins = 10):
        '''
        Question 6: Generates one histogram per region
        Each histogram represents distribution of incomes in that region, across specified number of bins
        To allow for comparison between regions (Question 9), y and x axes are set to 
        '''
        
        by_region = self.data.groupby("Region")
        
        # to allow for comparison between regions (Question 9), calculate values to use as xlim and ylim 
        # for all of the plots. If .plot automatically set x and y axes for each plot, they will 
        # not necessarily be the same and visual comparison of graphs will be difficult
        max_income = self.data["Income"].max()
        max_region_count = max([len(by_region.get_group(region)) for region in by_region.groups.keys()]) / (bins / 2)
        
        ### generate graphs, label and set the axes, and save
        for region in by_region.groups.keys():            
            current_region = by_region.get_group(region) # dataframe for the region
            
            region_plot = current_region.plot.hist(bins = bins, title = "Distribution of Income in Region: {}, {}".format(region, self.year), grid = True)
            
            plt.xlabel("Income Ranges")
            plt.ylabel("Number of Countries that Fall in Income Range")
            
            # set axes for consistency across all plots
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