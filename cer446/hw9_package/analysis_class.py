'''
Created on Dec 1, 2016

@author: Caroline
This class uses the functions in year_level and region_level
and it creates two files: (1) a boxplot for each region in a certain year and
(2) a density plot for each regions for a certain year
'''

import matplotlib.pyplot as plt
import year_level as yr
import region_level as r
import load_data as l

class Analysis():
    def __init__(self, year, data):
        self.year = yr.validate_year(year)
        self.data = data
        self.regions = list(set(l.countries['Region']))
        
    def create_regional_boxplot(self):
        '''Produces a boxplot for each region for a certain year'''

        income_for_year = r.merge_by_year(self.year, self.data)

        by_region = []

        for i in range(0, len(self.regions)):
            by_region.append(list(income_for_year[income_for_year['Region'] == self.regions[i]]['Income'].dropna().values))
    
        plt.figure(figsize = (10,6))
        boxplot = plt.boxplot(by_region, labels = self.regions)
        plt.savefig('boxplot_' + str(self.year), format = 'png')
        return boxplot
            
    def plot_all_regional_distributions(self):
        '''Produces a page of 6 histograms with a distribution curve, one for each region'''
    
        num_regions = len(self.regions)
        start = num_regions*100 + 10 + 1
        subplots = list(range(start, start+num_regions))
        
        region_subplotnum = list(zip(subplots, self.regions))
        
        for i in range(0, len(region_subplotnum)):
            r.plot_regional_distribution(self.year, region_subplotnum[i][1], region_subplotnum[i][0])
            
        plt.subplots_adjust(wspace = .4, hspace = .4)
        
        fig = plt.gcf()
        fig.set_size_inches(10.5, 20)
        
        plt.savefig('regional_distributions_' + str(self.year), orientation='portrait', papertype='letter', format = 'png')