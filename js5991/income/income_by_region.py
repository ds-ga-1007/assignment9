'''
Created on Dec 3, 2016

@author: Jingyi Su js5991
@description: This class has two main functions. 1) boxplot: it plots a boxplot of income for a given year by region 2) histogram: it plots a histogram of income for a given year by region
              Both functions allow users to enter a path for saving the plot, otherwise, the plot will be displayed. 

'''
from income.load_display_data import merge_by_year
import matplotlib.pyplot as plt

class income_by_region:
    '''
    This class explores the distribution of GDP per capita and display the distributions by region with histograms and boxplots
    '''
    def __init__(self):
        '''
        Constructor: no assignment included in this class
        '''
        
    def boxplot(self, year, path=None):
        '''
        This function creates a boxplot of income by region for the given year. The plot will be saved to path if specified, otherwise, it will be shown
        '''
        mergedData=merge_by_year(year).dropna()
        plot=mergedData.boxplot(by="Region", rot=25).get_figure()
        
        if path==None:
            plot.show()
        else:
            plot.savefig(path)
        
    
    def histogram(self, year, path=None):
        '''
        This function creates a boxplot of income by region for the given year. The plot will be saved to path if specified, otherwise, it will be shown
        '''
        mergedData=merge_by_year(year).dropna()
        mergedData.hist("Income", by="Region", bins=20, xrot=25, xlabelsize=8, figsize=(8,8))
        
        if path==None:
            plt.show()
        else:
            plt.savefig(path)
         
