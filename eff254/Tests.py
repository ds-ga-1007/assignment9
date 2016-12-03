# -*- coding: utf-8 -*-

import unittest
import Utils as ut
import pandas as pd
import numpy as np

class myTestsforImportCSV(unittest.TestCase):
    
    def test_function(self):
        self.assertEqual(ut.importMyCsv("countries").columns.values.all(), np.array(['Country', 'Region'], dtype=object).all())
        self.assertEqual(ut.importMyCsv("countries").size, 388)
        self.assertEqual(ut.importMyCsv("countries").shape, (194, 2))
        
class myTestsforImportXLSX(unittest.TestCase):
    
    def test_function(self):
        self.assertEqual(ut.importMyExcel("indicator gapminder gdp_per_capita_ppp").size, 55380)
        self.assertEqual(ut.importMyExcel("indicator gapminder gdp_per_capita_ppp").shape, (260, 213))
        self.assertEqual(ut.importMyExcel("indicator gapminder gdp_per_capita_ppp").columns.values.all(), np.arange(1800, 2013).all())
        
         
class myTestsforStackUnstack(unittest.TestCase):
    
    def setUp(self):
        self.mockData_1 = pd.DataFrame([1,2,3,4], columns=["HelloWorld"], index=["foo1", "foo2", "foo3", "foo4"])
        self.mockData_2 = pd.DataFrame([1,2,3,4, np.nan], columns=["HelloWorld"], index=["foo1", "foo2", "foo3", "foo4", "foo5"])
        self.income = ut.importMyExcel("indicator gapminder gdp_per_capita_ppp")
        
    def test_function_mocks(self):
        self.assertEqual(ut.stackUnstack(self.mockData_1).columns.values.all(), np.array(['foo1', 'foo2', 'foo3', 'foo4'], dtype=object).all())
        self.assertEqual(ut.stackUnstack(self.mockData_1).index.values.all(), np.array(['HelloWorld'], dtype=object).all())
        self.assertEqual(ut.stackUnstack(self.mockData_2).columns.values.all(), np.array(['foo1', 'foo2', 'foo3', 'foo4', 'foo5'], dtype=object).all())

    def test_function_real(self):
        self.assertEqual(ut.stackUnstack(self.income).shape, (213, 260))
        self.assertEqual(ut.stackUnstack(self.income).size, self.income.size)
  
  
class myTestsforStringToNumber(unittest.TestCase):
    
    def test_function(self):
        self.assertEqual(ut.stringToNumber("9"), 9)
        
    def raiseException(self):
        self.assertRaises(ut.stringToNumber("foo"), ut.numberNotANumber())
        

class myTests_TestIfInIndex(unittest.TestCase):
    
    def setUp(self):
        self.mockData1 = pd.DataFrame([1,2,3,4, np.nan], columns=["HelloWorld"], index=[1, 2, 3, 4, 5])
        self.mockData2 = pd.DataFrame([1,2,3,4, np.nan], columns=["HelloWorld"], index=["foo1", "foo2", "foo3", "foo4", "foo5"])
    
    def test_function_mocks(self):
        self.assertTrue(ut.TestIfInIndex("foo1", self.mockData2))
        self.assertTrue(ut.TestIfInIndex(1, self.mockData1))
        self.assertFalse(ut.TestIfInIndex("foo1", self.mockData1))
        self.assertFalse(ut.TestIfInIndex(1, self.mockData2))


class myTestsMergeByYear(unittest.TestCase):
    
    def setUp(self):
        self.income = ut.stackUnstack(ut.importMyExcel("indicator gapminder gdp_per_capita_ppp"))
        self.countries = ut.importMyCsv("countries")
        
    def test_1990(self):
        self.assertEqual(ut.merge_by_year(1990, self.income, self.countries).columns.values.all(), np.array(['Income', 'Country', 'Region'], dtype=object).all())
        self.assertEqual(ut.merge_by_year(1990, self.income, self.countries).size, 582)
        self.assertEqual(ut.merge_by_year(1990, self.income, self.countries).shape, (194, 3))
        
    def test_2012(self):
        self.assertEqual(ut.merge_by_year(2012, self.income, self.countries).columns.values.all(), np.array(['Income', 'Country', 'Region'], dtype=object).all())
        self.assertEqual(ut.merge_by_year(2012, self.income, self.countries).size, 582)
        self.assertEqual(ut.merge_by_year(2012, self.income, self.countries).shape, (194, 3))        
 

if __name__ == '__main__':
    unittest.main()