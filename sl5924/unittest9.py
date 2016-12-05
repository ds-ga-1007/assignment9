'''
This is the test module of the assingment9 program
Created on 2016/12/1
Version: 1.0
@author: liusheng
ShengLiu Copyright 2016-2017
'''
from data_exploratory import *
import sys
import unittest
from data import *

class  utest(unittest.TestCase):
	def setUp(self):
		#print ('Setting up ....')
		pass

	def test_merge_by_year(self):
		self.assertEqual(merge_by_year(2000).columns.values[0],'Country')
		self.assertEqual(merge_by_year(2000).columns.values[1],'Region')
		self.assertEqual(merge_by_year(2000).columns.values[2],'Income')

	def test_data_explore(self):
		test = data_explore(2007)
		self.assertEqual(test.year,2007)
		self.assertEqual(test.merge_DataFrame.columns.values[0],'Country' )
		self.assertEqual(test.merge_DataFrame.columns.values[1],'Region' )
		self.assertEqual(test.merge_DataFrame.columns.values[2],'Income' )


if __name__ == '__main__':
	unittest.main()

