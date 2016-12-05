'''
Main script:
This project presents the distribution of income per person around the world by the dataset:
 countries.csv
 indicator gapminder gdp_per_capita_ppp.xlsx
It has two main functions:
 1 Display the histogram of income per person of all countries in the year user inputed 
 2 Generate reports of income by region from 2007-2012 
 

Created on Nov 28, 2016
Last Modified        : 
Version        : 1.0
@author: Nan Wu
@email: nw1045@nyu.edu

'''

import sys
import os
from inspect import getsourcefile
from os.path import abspath
from GlobalIncome_Main import GlobalIncome_Display
from UserDefinedError import QuitProcess
if __name__ == '__main__':
    try:
        DataPath=abspath(getsourcefile(lambda:0))
        DataPath=DataPath[:-14]
        DataPath=''.join([DataPath,'dataset/'])
        while True:
            try:
                GlobalIncome_Display(DataPath)
                break
            except FileNotFoundError:
                DataPath=input("Please Reset the data path to:")
                if DataPath=='quit':
                    raise QuitProcess
                
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    except QuitProcess:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    