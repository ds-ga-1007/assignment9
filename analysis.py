import pandas as pd
import matplotlib.pyplot as plt

class analysis:
    '''
    This class outputs histograms & boxplots to visualize distributions of
    income per person by region for the year indicated by the user.
    '''
    def __init__(self, merged, year):
        "Initialize these two variables"
        self.merged = merged
        self.year = year
        
    def histogram_region(self):
        '''Output a histogram representing income distribution by region'''
        for r in self.merged['Region'].unique():
            plt.hist(self.merged[self.merged["Region"]==r]["Income"].dropna().reset_index(drop=True), alpha=0.5, label=r)

        plt.legend()
        plt.title('Income Distribution By Region: '+str(self.year))
        plt.xlabel('Income Per Person')
        plt.ylabel('Frequency')
        plt.savefig('Histogram Of Income By Region: '+str(self.year)+'.png')  
        plt.close()
        
    def boxplot_region(self):
        '''Output a boxplot representing income distribution by region'''
        self.merged.boxplot(column='Income', by = 'Region', figsize=(8,5))
        
        plt.title('Income Per Person: '+str(self.year))
        plt.ylabel('Income Per Person')
        plt.savefig('Boxplot Of Income By Region: '+str(self.year)+'.png')

        plt.close()
