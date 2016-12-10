import pandas as pd
import matplotlib.pyplot as plt
from income.functions import *
from income.exceptions import *


class income_plots(object):
    '''This class uses exploratory data analysis tools (histograms and boxplots) to graphically
explore the distribution of the income per person by region data set from the merge_by_year(year)
function for a given year. Individual files are saved as .pdf files.'''
    def __init__(self, year):
        self.year = int(year)
        
    def plot_box(self):
        '''This function plots the boxplots of the income per person across regions.'''
        plt.clf()
        merge_by_year(self.year).boxplot(column='Income', by='Region', fontsize=7)
        plt.title('')
        plt.ylabel('Income')
        plt.suptitle("Boxplots of Regions' Income for Year " + str(self.year), size=12)
        plt.savefig("Boxplots of Regions' Income for Year " + str(self.year) + ".pdf")
        
    def plot_hist(self):
        '''This function plots the histograms of the income per person across regions.'''
        self.income_df = merge_by_year(self.year).groupby(by='Region')
        plt.clf()
        self.income_df.Income.plot.hist(stacked=True, bins=30, alpha=0.6)
        plt.xlabel('Income')
        plt.legend(loc = 'upper right')
        plt.title("Histograms of Regions' Income for Year " + str(self.year), size=12)
        plt.savefig("Histograms of Regions' Income for Year " + str(self.year) + ".pdf")