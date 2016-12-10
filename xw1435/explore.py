import matplotlib.pyplot as plt
from function import merge_by_year

class explore():
    '''
    Provide a class that uses exploratory data analysis tools (histograms and boxplots) to graphically explore 
    the distribution of the income per person by region data set for a given year. 
    Save these graphs to individual files.
    '''

    def __init__(self, year):
        '''
        Constructor
        '''
        self.year = year
        self.data = merge_by_year(year)
    
    def draw_boxplot(self):
        boxplot = self.data.boxplot(by = 'Region', figsize = (10,10), rot = 30)
        plt.title('Income per person by region for year ' + str(self.year), fontsize = 15)
        plt.savefig('boxplot_' + str(self.year)+ '.pdf')
        return boxplot
    
    def draw_histogram(self):
        histogram = self.data.hist(by = 'Region', figsize = (10,20), color = 'darkviolet', bins= 50, rot = 30)
        plt.savefig('histogram_' + str(self.year)+ '.pdf')
        return histogram
        