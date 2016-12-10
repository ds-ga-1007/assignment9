import pandas
import matplotlib.pyplot as plt

class GDPAnalysis(object) :
    """Class used to perform analyses on the data and output plots in pdf format"""
    def __init__(self,year,data) :
        self.year = year
        self.data = data
    
    def lowIncomePlot(self) :
        """Generates and saves histograms of regions having GDP per capita less than 3000"""
        d = self.data
        pandas.DataFrame(d.loc[d['Income']<3000]['Region']).apply(pandas.value_counts).plot(kind='bar',rot=0)
        plt.title('# of countries with per capita GDP < 3000 in the year %d' % self.year)
        plt.savefig('low income histogram %d' % self.year, format='pdf')
        
    def boxPlot(self):
        """Generates and saves boxplots of income data for each region"""
        d = self.data
        self.data.boxplot('Income','Region', fontsize=10)
        plt.savefig('income boxplot by region %d' % self.year, format='pdf')

    def performAnalysis(self) :
        """Calls the lowIncomePlot() and boxPlot() functions"""
        self.lowIncomePlot()
        self.boxPlot()
        
