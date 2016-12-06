'''
Created on 2016.12.3

@author: xulei
'''
from load_data import *
from excep_class import *

class Year:

    def __init__(self, year):
               
        if (int(year)> income.index.max() or int(year)< income.index.min()):
            raise rangeException() 
        else:
            self.yr= int(year)
        

              

        