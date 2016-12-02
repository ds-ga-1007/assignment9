# Author: Leslie Huang (lh1036)
# Description: Custom errors for handling user input

class InvalidYearError(Exception):
    '''
    Error if user inputs a year not contained in dataset
    '''
        
    def __str__(self):
        return "Invalid year."

class QuitError(Exception):
    '''
    Error if user ends program with input "finish" or if Keyboard Interrupt
    '''

    def __str__(self):
        return "Goodbye."