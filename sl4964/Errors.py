'''
Created on Dec 4, 2016

@author: ShashaLin
'''
class Errors(Exception):
    pass

class InputError(Errors):
    def __init__(self):
        print('Not valid year.')

