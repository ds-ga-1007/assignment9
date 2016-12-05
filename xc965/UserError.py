'''
This module contains user's self-defined exceptions.

@author: Xianzhi Cao (xc965)
'''

# Error: Input is empty.
class EmptyInputError(Exception):
    def __str__(self):
        return 'Input Error! Empty input.\n'


# Error: Main module input does not match year format.
class InputFormatError(Exception):
    def __str__(self):
        return 'Input Format Error! Please enter a year.\n'


# Error: Main module input value exceeds valid range.
class InputValueError(Exception):
    def __str__(self):
        return 'Input Value Error! The year should be between 1800 and 2012.\n'


# Error: Main module input value exceeds valid range.
class InvalidInputError(Exception):
    def __str__(self):
        return 'Invalid Input! Please enter \'y\' to continue; \'n\' or \'q\' to quit.\n'
