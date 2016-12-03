'''
Created on Dec 2, 2016
This test of the merge_by_year function randomly chooses
a year 10 times and ensures that the country and region
columns have the correct data, regardless of the year.
@author: da1933
'''
import unittest
import graph_functions
import random

class Test(unittest.TestCase):

    def testMerge(self):
        for i in enumerate(range(10)):
            a = graph_functions.merge_by_year(random.randrange(1800,2013,1))
            self.assertEqual(a.ix[0][1], 'AFRICA')
            self.assertEqual(a.ix[100][0], 'Finland')


if __name__ == "__main__":
    unittest.main()