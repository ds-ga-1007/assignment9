'''
Created on Dec 3, 2016

@author: Zahra
'''

import matplotlib.pyplot as plt

class explore():
    '''a class that uses exploratory data analysis tools (histograms and boxplots) to graphically explore the distribution 
    of the income per person by region data set from question 5 for a given year. Save these graphs to individual files..'''
    
    def __init__(self, data, year):
        self.data = data
        self.year = year
    
    def box(self):
        boxGraph = self.data.boxplot(by = 'Region', figsize = (12,10), fontsize = 12)
        plt.title("Income per person by region for year " + str(self.year), fontsize = 20)
        filename = 'boxplot_' + str(self.year)+ '.pdf'
        plt.savefig(filename)
        return boxGraph
    
    def histo(self):
 
        histGraph = self.data.hist(by = 'Region', figsize = (12,18), bins = 30, range=[(self.data['Income']).min(), (self.data['Income']).max()])
        plt.suptitle("Income per person by region for year " + str(self.year), fontsize = 20)
        filename = 'histogram_' + str(self.year)+ '.pdf'
        plt.savefig(filename)
        return histGraph


        