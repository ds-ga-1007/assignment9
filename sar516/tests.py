import unittest
import pandas as pd
import numpy as np
from Income import Yearly_Income
from assignment9 import merge_by_year

class Test(unittest.TestCase):
    
    countries = pd.read_csv("../countries.csv", index_col = 0)
    income = pd.read_excel("../indicator gapminder gdp_per_capita_ppp.xlsx", index_col = 0)

    countries = countries.transpose()
    income = income.transpose()
    
    data = merge_by_year(countries, income, 2001)

    def income_test1(self) :
        """This function tests to see that the proper Error is raised when something besides a dataframe              is passed for data into the class"""
        with self.assertRaise(ValueError) as error:
            Yearly_Income("a", 2001)
        self.assertTrue("Invalid type for data passed into this class" in str(error.exception))
        
    def income_test2(self) :
        """This function tests to see that the proper Error is raised when something besides a number             is passed for year into the class"""
        with self.assertRaise(ValueError) as error:
            Yearly_Income(data , "a")
        self.assertTrue("Improper type for year passed into this class" in str(error.exception))
        
    def income_test3(self) :
        """This function tests to see that the proper Error is raised when something besides a proper year            is passed for year into the class"""
        with self.assertRaise(ValueError) as error:
            Yearly_Income(data , 1)
        self.assertTrue("Invalid year passed into this class" in str(error.exception))
        
        
if __name__ == '__main__':
    unittest.main()        