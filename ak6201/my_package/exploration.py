'''
Created on Dec 5, 2016

@author: Akash
'''
import matplotlib.pyplot as plt

class exploratory_analysis:
        
    def plt_Histogram(self, data, year):
        data.hist(by='Region', figsize=(12,16)) # to display a Histogram for every region (continent) 
        plt.suptitle('Income per person by Region for the year ' + str(year))
        filename = '{0}{1}{2}'.format('Histogram_',str(year),'.pdf')
        plt.savefig(filename) # the plot is saved in the same path
         
    def plt_Boxplot(self, data, year):
        data.boxplot(column='Income', by='Region', figsize=(12,10), fontsize=12) # to display a Boxplot for every region (continent)
        plt.title('Income per person by Region for the year ' + str(year))
        plt.xlabel('Income_distribution')
        plt.ylabel('Count')
        filename = '{0}{1}{2}'.format('Boxplot_',str(year),'.pdf')
        plt.savefig(filename) # the plot is saved in the same path