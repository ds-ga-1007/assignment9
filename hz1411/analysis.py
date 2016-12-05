import matplotlib.pyplot as plt

class analysis:
    '''Provide a class that draws histograms and boxplots to explore 
    the distribution of the income per person by region for a given year,
    and save figures to files'''
    def __init__(self, merged, year):
        # constructor that reads the merged dataframe and the given year
        self.merged = merged
        self.year = year
    def histogram_by_region(self):
        '''Plot a stacked histogram for income distribution grouped by region'''
        for region in self.merged['Region'].unique():
            plt.hist(self.merged[self.merged["Region"]==region]["Income"].dropna().reset_index(drop=True), alpha=0.5, label=region)
        plt.legend()
        plt.xlabel('Income per capita')
        plt.ylabel('Count')
        plt.title('Income distribution by region in '+str(self.year))
        plt.savefig('Histogram of income by region in '+str(self.year)+'.png')  
        plt.close()
    def boxplot_by_region(self):
        '''Plot a boxplot for income distribution grouped by region'''
        self.merged.boxplot(column='Income',by = 'Region',figsize=(8,5))
        plt.title('Income per capita in '+str(self.year))
        plt.ylabel('Income per capita')
        plt.savefig('Boxplot of Income by region in '+str(self.year)+'.png')
        plt.close()
