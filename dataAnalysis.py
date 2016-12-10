# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 10:43:13 2016

@author: kevinyan
"""

import matplotlib.pyplot as plt



class dataAnalysis():
    
    def __init__(self, year):
        self.year = year
    
   
    def histogram(self, income):
        """
        The function plots a histogram of the distribution of the income per person by region data 
        """
        income.hist(by = 'Region', figsize = (12, 12), fontsize = 12)
        plt.title("histogram of the distribution of the income in " + str(self.year))
        plt.xlabel('Region')
        plt.ylabel('Income Per Person')
        plt.savefig('histogram in' + str(self.year) + '.pdf')
        plt.show()
    

    def boxplot(self, income):
        """
         The function plots a boxplot to show the distribution of the income per person by region data 
        """
        income.boxplot(by = 'Region', figsize = (12, 12), fontsize = 12)
        plt.title("boxplot of the distribution of the income in " + str(self.year))
        plt.xlabel('Region')
        plt.ylabel('Income Per Person')
        plt.savefig('boxplot in ' + str(self.year) + '.pdf')
        plt.show()