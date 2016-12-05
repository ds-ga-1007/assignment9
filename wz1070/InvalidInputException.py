# This is the class of user defined exception when there is an invalid input. 
class InvalidInputException(Exception):
    
    # Throw specific exception when needed. 
    def __str__(self):
        return 'Invalid input, enter a year between 1800 and 2012, or \'finish\' to exit'