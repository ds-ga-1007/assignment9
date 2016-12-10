'''
Created on Dec 2, 2016
References used in this module:
http://stackoverflow.com/questions/20656663/matplotlib-pandas-error-using-histogram
http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.reindex.html
@author: da1933
'''

import matplotlib.pyplot as plt
from graph_functions import merge_by_year

#This class is defined by region
class Region:
  
    def __init__(self, region):
        self.region = region
    
    #The class has one method that generates a boxplot and a histogram for 
    #a specified year in the across the region of the class
    def save_graphs(self, year):
        plt.close('all')
        year_data = merge_by_year(int(year))
        label = "Per capita incomes in " + self.region + ' in ' + str(year)
        data = year_data[year_data.Region == self.region].reset_index()
        
        plt.boxplot(data['Income'])
        plt.xlabel(label)
        plt.ylabel('Income Distribution')
        plt.savefig(str(self.region) + ' income per capita boxplot from ' + str(year) + '.pdf', format='pdf')
        plt.close('all')
        
        plt.hist(data['Income'].dropna())
        plt.xlabel(label)
        plt.ylabel('Number of countries')
        plt.savefig(str(self.region) + ' income per capita histogram from ' + str(year) +'.pdf', format='pdf')

