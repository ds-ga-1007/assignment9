""" Question 6, class analysis_tools which will be used to create histograms and boxplots by region """ 

import pandas as pd
import matplotlib.pyplot as plt
from func import *


# Q6
class analysis_tools():
     def __init__(self, year):
                self.year = year
     
    # refer to online pandas 0.19.1 documentation
    # function to create histograms to explore the distribution of the income per person by region
     def hist_plot(self):
            merged_data = merge_by_year(self.year)
            merged_data.hist(column='Income',by='Region',bins=50,xlabelsize=6,ylabelsize=6,grid=True)
            plt.savefig('Histogram of the distribution of the income per person by region in year {0}.pdf'.format(self.year))
            plt.close()
            
    # function to create boxplots to explore the distribution of the income per person by region
     def box_plot(self):
            merged_data = merge_by_year(self.year)
            merged_data.boxplot(column='Income',by='Region',grid=True,fontsize=7)
            plt.savefig('Boxplot of the distribution of the income per person by region in year {0}.pdf'.format(self.year))
            plt.close()
