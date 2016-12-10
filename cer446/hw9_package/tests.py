'''
Created on Dec 4, 2016

@author: Caroline
'''

import analysis_class as ac
import load_data as l
import os
import region_level as r

#can use os to verify that the files are there (won't check the contents)

import unittest

class AnalysisTestCase(unittest.TestCase):
    def setUp(self):
        self.test_analysis = ac.Analysis(2005, l.income)
        self.boxplotresults = self.test_analysis.create_regional_boxplot()
        self.test_analysis.plot_all_regional_distributions()
        self.files = os.listdir()

    def tearDown(self):
        os.remove('boxplot_' + str(self.test_analysis.year))
        del self.test_analysis

class Analysis_class_test(AnalysisTestCase):
    '''Verifies that create_regional_boxplot and create_regional_distributions successfully create files'''
    def test_regional_boxplot(self):
        self.assertTrue('boxplot_' + str(self.test_analysis.year) in self.files) #verifies a file was created
        self.assertEqual(len(self.boxplotresults['boxes']), 6) #verifies there are 6 boxes in the plot
    def test_regional_distributions(self):
        self.assertTrue('regional_distributions_' + str(self.test_analysis.year) in self.files)
        
class MergeByYearTestCase(unittest.TestCase):
    def setUp(self):
        self.test_merged = r.merge_by_year(2005, l.income)
    
    def tearDown(self):
        del self.test_merged
        
class Merge_by_year_test(MergeByYearTestCase):
    def test_merge_by_year_columns(self):
        '''Verifies that the merged data set has the right columns'''
        self.assertEqual(list(self.test_merged.columns), ['Country', 'Region', 'Income'])
    
    def test_merge_by_year_nonulls(self):
        '''Verifies that the merged data set doesn't have any nulls'''
        self.assertFalse(True in self.test_merged.isnull())
        
class LoadTestCase(unittest.TestCase):
    def setUp(self):
        self.test_load = l.load('indicator gapminder gdp_per_capita_ppp.xlsx')
    
    def tearDown(self):
        del self.test_load
        
class Load_test(LoadTestCase):
    def test_load_index(self):
        self.assertFalse(False in (self.test_load.index == range(1800, 2013)))
        
#what else should I do? since I can get info from the charts, what info do I want from them?

#maybe just make sure that data plotted isn't full of 0's and nulls and it's the expected length

#so for the boxplot method, verify that we have a non-zero boxplot for each region

#and for the distribution method, verify that we have a non-zero line in each one.

#can use patches.get_height to get the height of a histogram

#but we didn't use matplotlib for this, we used the series method

#plot_regional_distribution?
#plot_distribution?

#http://matplotlib.org/api/pyplot_api.html


if __name__ == '__main__':
    unittest.main()

#can verify that plot_requested_distributions throws errors