'''
This module contains user defined errors.
    InputError
    QuitProcess
Created on Nov 28, 2016
Last Modified        : 
Version        : 1.0
@author: Nan Wu
@email: nw1045@nyu.edu
'''

class InputError(Exception):
    # Handling meaningless Input
    def __str__(self):
        return 'Invalid Input!\n Please according to the instruction!'

class QuitProcess(Exception):
    # Quit the Process
    pass
    