from UserDefinedError import *

'''
this class will check if the input is incorret
'''
def check_input(year):
    try:
        int(year)
    except ValueError:
        raise NotInterror("Not a Integar!")
    
    if int(year)<1800 or int(year)>2012:
        raise OutofRangeError(year, 1800, 2012)
    