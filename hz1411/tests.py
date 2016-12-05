import unittest
from data import *

class SimpleTest(unittest.TestCase):

	def test_merge(self):
# Test merge_by_year(year) function in data.py'''
		for year in range(1990,1995):
			merged = merge_by_year(year)
			self.assertEqual(merged.columns.tolist(), ['Country', 'Region', 'Income'])

		self.assertEqual(merge_by_year(1926).iloc[0]['Country'],'Algeria')
		self.assertEqual(merge_by_year(1945).iloc[30]['Region'],'AFRICA')

if __name__=="__main__":
	unittest.main()

