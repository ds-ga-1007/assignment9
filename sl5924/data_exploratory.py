"""
This module was used to explore dataset

Created on 2016/12/03
Version: 1.0
@author: Sheng Liu
ShengLiu Copyright 2016-2017
"""
from data import *
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
class data_explore:
	def __init__(self,year):
		self.merge_DataFrame = merge_by_year(year)
		self.year = year

	def save_histogram(self):
		'''
		This method uses histogram to explore the distribution of the income, and save the final histograms.
		'''
		print(">>>>>>>>>>>>>>>>>>>Saving Histograms from year 2007 to 2012>>>>>>>>>>>>>>>>>>>>")
		fig, axis = plt.subplots(nrows = 2, ncols = 3,figsize = (20,10))
		fig.suptitle(str(self.year) + ' Histogram in regions',fontsize = 30)
		i,j = 0,0
		for region in np.unique(self.merge_DataFrame['Region'])[0:3]:
			merge_DataFrame_in_region = self.merge_DataFrame[self.merge_DataFrame['Region'] == region][['Country','Income']]
			merge_DataFrame_in_region.hist(bins = 10, ax = axis[i,j])
			axis[i,j].set_title(str(region))
			axis[i,j].set_xlabel('Income per person')
			axis[i,j].set_ylabel('Count')
			j=j+1
		i,j = 1,0
		for region in np.unique(self.merge_DataFrame['Region'])[3:6]:
			merge_DataFrame_in_region = self.merge_DataFrame[self.merge_DataFrame['Region'] == region][['Country','Income']]
			merge_DataFrame_in_region.hist(bins = 10, ax = axis[i,j],figsize =(3,3))
			axis[i,j].set_title(str(region))
			axis[i,j].set_xlabel('Income per person')
			axis[i,j].set_ylabel('Count')
			j=j+1
			
		plt.savefig(str(self.year)+'Histogram for all regions')

	def save_boxplots(self):
		'''
		This method uses boxplots to explore the distribution of the income, and save the final histograms.
		'''
		print(">>>>>>>>>>>>>>>>>>>Saving boxplot from year 2007 to 2012>>>>>>>>>>>>>>>>>>>>")
		self.merge_DataFrame.groupby(['Region']).boxplot(fontsize = .01, figsize = (8,10))
		plt.suptitle(str(self.year) + ' boxplot of per person income in All Region' )
		plt.savefig(str(self.year)+'boxplot for all regions')

if __name__ == '__main__':
	year = 2007
	data_explore(year).save_histogram()
	data_explore(year).save_boxplots()
