'''
Created on 2016.12.3

@author: xulei
'''

class rangeException(Exception):
    def __str__(self):
        return 'The year is out of valid range'