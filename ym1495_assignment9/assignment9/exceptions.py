'''
Created on Dec 5, 2016

@author: muriel820
'''

class invalid_input(Exception):
    '''
    classdocs
    '''
    def __repr__(self, params):
        return "Invalid Year Input!\n"

        