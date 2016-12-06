'''
Created on Dec 5, 2016

@author: felix
'''
import matplotlib.pyplot as plt

class Distribution:
    '''
    Question 6:
    Provide a class that uses exploratory data analysis tools (histograms and boxplots) to graphically 
    explore the distribution of the income per person by region data set from question 5 for a given year. 
    Save these graphs to individual files.
    '''

    def __init__(self, data, year):
        '''
        Constructor
        '''
        self.year = year
        self.data = data
        
    def plot_box(self):
        df = self.data
        # Replace the names so that the xlabels look less crowded
        df.replace(['NORTH AMERICA', 'SOUTH AMERICA'], ['N. AMERICA', 'S. AMERICA'], inplace=True)
        df.boxplot(by = 'Region')
        plt.savefig('./Plots/'+'Boxplot for year '+ str(self.year) +'.pdf')
        plt.show()
        plt.close()
        
    def plot_hist(self):
        df = self.data
        df.replace(['NORTH AMERICA', 'SOUTH AMERICA'], ['N. AMERICA', 'S. AMERICA'], inplace=True)
        df.hist(by = 'Region', figsize = (8.5, 11)) # set figure size so that subplots not overlapping
        plt.savefig('./Plots/'+'Histogram for year '+ str(self.year) +'.pdf')
        plt.show()
        plt.close()       