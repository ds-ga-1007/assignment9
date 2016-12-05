import matplotlib.pyplot as plt

'''The self-defined module initialized a class tool to better draw boxplots and histograms'''

class tool:
    def __init__(self, year, data):
        self.year = year
        self.data = data


    def histogram(self):
        gdp_by_region = self.data.groupby('Region').Income.apply(list)
        gdp_values = list(gdp_by_region.values)
        gdp_region = list(gdp_by_region.index)
        plt.hist(gdp_values, label=gdp_region)
        plt.xlabel('GDP per Capita')
        plt.ylabel('Count')
        plt.title('Number of Countries in Each Continent')
        plt.legend(loc='upper right')
        plt.show()
        plt.savefig('Histogram of Year '+ str(self.year) )
        plt.close()


    def boxplot(self):
        self.data.boxplot('Income', by ='Region',rot = 60)
        plt.xlabel('Distribution of Income/person at a Given Year By Continent')
        plt.ylabel('GDP per Capita')
        plt.show()
        plt.savefig('Boxplot of Year ' + str(self.year))
        plt.close()


