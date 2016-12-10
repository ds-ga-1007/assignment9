'''
Created on 2016.12.3

@author: xulei
'''
from load_data import *
from pandas.io.wb import country_codes

class Region_Income:

    def __init__(self, year):
        
        self.data= merge_by_year(year)
        self.data.hist(by='Region',xrot=1,xlabelsize=5)
        plt.savefig('histogram for year {}.pdf'.format(year))
        self.data.boxplot(by='Region')
        plt.savefig('boxplot for year {}.pdf'.format(year))
        

              
        