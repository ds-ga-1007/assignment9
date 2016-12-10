from Func.Func import *

class AnalysisTools():
    def __init__(self, year):
        
        '''Constructor'''
        self.year = year
        
    def hist_plot(self):
        
        '''
        Function hist_plot create histogram to explore the distribution of the income per person by region data set.
        
        return: NONE
            save graphs in .pdf files
        '''
        data = merge_by_year(self.year)
        data.hist(column = 'Income', by = 'Region', bins = 50, xlabelsize=6, ylabelsize=6)
        plt.title('Histogram of Income in year {0}.pdf'.format(self.year))
        plt.xlabel('Income')
        plt.ylabel('Frequency')
        plt.savefig('Histogram of Income in year {0}.pdf'.format(self.year))
        plt.close()
        
    def box_plot(self):    
        data = merge_by_year(self.year)
        data.boxplot(column='Income',by='Region', fontsize = 7)
        plt.savefig('Boxplot of Income in year {0}.pdf'.format(self.year))
        plt.close()