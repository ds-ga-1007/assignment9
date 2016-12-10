import matplotlib.pyplot as plt

# This is the class of the exploratory data analysis tools. 
class DataAnalysis:
    
    # Constructor of the object
    def __init__(self, year):
        self.year = year
    
    # Plot and save the histogram of the Income per person grouped by the region. 
    def histogram(self, data):
        data.hist('Income', by = 'Region', figsize = (10, 10))
        plt.title("Histogram of income by region of year " + str(self.year))
        plt.xlabel('Region')
        plt.ylabel('Income Per Person')
        plt.savefig('histogram of year ' + str(self.year))
        plt.show()
    
    # Plot and save the boxplot of the Income per person grouped by the region. 
    def boxplot(self, data):
        data.boxplot('Income', by = 'Region', figsize = (10, 10))
        plt.title("boxplot of income by region of year " + str(self.year))
        plt.xlabel('Region')
        plt.ylabel('Income Per Person')
        plt.savefig('boxplot of year ' + str(self.year))
        plt.show()