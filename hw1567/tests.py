import unittest
from assignment9 import *
import random
import numpy as np

class tests(unittest.TestCase):
	"""Unit-testing class that allows us to run tests with expected outcomes
	Run the test in the project's root directory
	with the following command:
		$ python3 -m unittest discover
	"""
	def test_merge_by_year(self):
		"""
		unit tests for testing merge_by_year function.
		Test the return dataset has the expected columns and the data in column is correct.
		"""
		countries, income = read_data()
		year = random.randrange(1800, 2012)
		merged_data = merge_by_year(year, countries, income)
		self.assertEqual(merged_data.columns.values.tolist(), ['Country', 'Region', 'Income'])


		merged_data = merged_data.set_index(np.arange(len(merged_data)))
		temp = True
		for i in range(len(merged_data)):
			temp = temp and (merged_data['Income'][i] in income[year].dropna().tolist())
		self.assertTrue(temp)

if __name__ == "__main__":
    unittest.main()