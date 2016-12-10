'''
Created on Dec 5, 2016

@author: sj238
'''
import matplotlib.pyplot as plt
import pandas as pd

class graphs(object):
    '''
    classdocs
    '''
    
    def __init__(self, data, year):
        '''
        Constructor
        '''
        self.year = year
        self.data = data
    
    def boxplot(self):
        self.data.boxplot('Income', by = 'Region')
        plt.title("Boxplot of income by region_"+str(self.year))
        plt.xlabel('Region')
        plt.ylabel('Income per person')
        print("close image to continue")
        plt.savefig('Boxplot of income per person from' + str(self.year) + '.pdf', format='pdf')
        plt.show()
        
    def histogram(self):
        
        plt.hist(self.data["Income"].dropna().values)
        plt.title("Histogram of income_"+str(self.year))
        plt.xlabel("Income per person")
        plt.ylabel("Number of countries")
        print("close image to continue")
        plt.savefig('Histogram of income per person from' + str(self.year) + '.pdf', format='pdf')
        plt.show()