import pandas as pd
import matplotlib.pyplot as plt

'''
Created on Dec 5, 2016

@author: sunyifu
'''

class analysis_data:
    '''
    classdocs
    '''


    def __init__(self, merged_data, year):
        '''
        Constructor
        '''
        self.merged_data = merged_data
        self.year = year
        
    
    def histogram(self):
        region_gdp = self.merged_data.groupby('Region').Income.apply(list)
        region_label = region_gdp.index.tolist()
        plt.hist(region_gdp, label=region_label)
        plt.xlabel('Income per person')
        plt.ylabel('Number of countries')
        plt.title('Histogram of income per person across regions ' )
        plt.legend()
        plt.savefig('Histogram for' + str(self.year) +'.pdf')
        plt.close()
        
        
        
    def boxplot(self):
        self.merged_data.boxplot('Income', by = 'Region')
        plt.title('Boxplot of income per person across regions')
        plt.ylabel('Income per person')
        plt.xlabel('Region')
        plt.savefig('Boxplot for' +str(self.year) + '.pdf')
        plt.close()
        
        



def read_data():
    countries = pd.read_csv('countries.csv')
    income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx', index_col = 0)
    income_transpose = income.T
    print('The head of income dataset:')
    print(income_transpose.head())
    return countries, income

def merge_by_year(year, countries, income):
    income_one_year = pd.DataFrame(income[year])
    merged_data = pd.merge(countries, income_one_year, left_on='Country', right_index=True).dropna()
    merged_data.columns = ['Country', 'Region', 'Income']
    return merged_data



def distribute_income(income,year):
    plt.hist(income.loc[year].dropna())
    plt.xlabel('Income per person')
    plt.ylabel('Number of countries')
    plt.title("Histogram of graphically distribution of the income per person in " + str(year))
    plt.show()
    plt.close()