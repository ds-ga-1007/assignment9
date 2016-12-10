'''
This module handles user defined exceptions/errors. 
'''

class InvalidInput(Exception):
    def __repr__(self):
        return "Value out of range"

