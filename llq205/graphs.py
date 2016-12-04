import pandas as pd
import matplotlib.pyplot as plt

class graphs:
    def __init__(self, year, data):
        '''Constructor'''
        self.year = year
        self.data = data
        
    def plotting(data1, data2, year):
        '''Explore the distribution of the income per person by region data set.
        Saved in pdf files'''
        
        plt.close('all')
        data = merge_by_year(data1, data2, year)
        region = data.groupby('Region').Income.apply(list)
        name = region.index.tolist()
        plt.hist(region.dropna(), label = name)
        plt.legend(loc = 'upper right')
        plt.title("Histogram of Income in year " + str(year))
        plt.xlabel("Income")
        plt.ylabel("Counts")
        plt.savefig("Histogram of Income in year " + str(year) + '.pdf')
        plt.close('all')
        
        box = data.boxplot(column='Income',by='Region')
        box.plot()
        plt.savefig("Boxplot of Income in year " + str(year) + '.pdf')
    
    
def income_per_person(data, year):
    '''Display the distribution of income per person 
    across all countries in the world for the given year'''
    
    plt.hist(data.ix[year].dropna(), alpha=0.9, color='blue')
    plt.title("Histogram of income per person in year " + str(year))
    plt.xlabel("Income")
    plt.ylabel("Counts")
    plt.show()
    plt.close()

    
def merge_by_year(data1, data2, year):
    '''Merge the countries and income data sets for any given year. 
    Return a DataFrame with three columns: Country, Region, and Income'''
    
    yearincome = pd.DataFrame(data2.ix[year])
    yearincome['Country'] = yearincome.index
    merge = pd.merge(data1, yearincome)
    merge = merge.rename(columns={year: 'Income'})
    return merge

