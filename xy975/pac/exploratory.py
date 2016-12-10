"""
This class turns a merged data in a given year into histograms and boxplots
by region.
"""
import matplotlib.pyplot as plt

class exploratory:
    def __init__(self, merge, year):
        self.merge = merge
        self.year = year

    def histograms(self):
        """
        histograms of ppp by region.
        """
        merge_cleaned = self.merge.dropna()
        plt.hist(merge_cleaned[merge_cleaned['Region']=='AFRICA']['Income'].reset_index(drop=True), alpha=0.6, label='AFRICA')
        plt.hist(merge_cleaned[merge_cleaned['Region']=='ASIA']['Income'].reset_index(drop=True), alpha=0.6, label='ASIA')
        plt.hist(merge_cleaned[merge_cleaned['Region']=='EUROPE']['Income'].reset_index(drop=True), alpha=0.6, label='EUROPE')
        plt.hist(merge_cleaned[merge_cleaned['Region']=='NORTH AMERICA']['Income'].reset_index(drop=True), alpha=0.6, label='NORTH AMERICA')
        plt.hist(merge_cleaned[merge_cleaned['Region']=='OCEANIA']['Income'].reset_index(drop=True), alpha=0.6, label='OCEANIA')
        plt.hist(merge_cleaned[merge_cleaned['Region']=='SOUTH AMERICA']['Income'].reset_index(drop=True), alpha=0.6, label='SOUTH AMERICA')
        plt.legend()
        plt.title("histogram in " + str(self.year) + " by region")
        plt.savefig("histogram in " + str(self.year) + " by region.pdf")
        plt.clf()
    
    def boxplot(self):
        """
        boxplot of ppp by region.
        """
        merge_cleaned = self.merge.dropna()
        merge_cleaned.boxplot('Income', by = 'Region',  fontsize=8)
        plt.yscale('log')
        plt.title("boxplot in " + str(self.year) + " by region")
        plt.savefig("boxplot in " + str(self.year) + " by region.pdf")
        plt.clf()