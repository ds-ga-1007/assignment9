'''
Created on Dec 5, 2016

@author: muriel820
'''

class MyError(Exception):
    '''Superclass of Exceptions'''
    pass
class invalid_input(MyError):
    def __str__(self):
        return 'Invalid Year Input! It should fall in the list of years\n'
    