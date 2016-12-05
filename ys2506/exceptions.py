
# Solution for DS-GA 1007 Assignment#9
# Author: Yanan Shi y2506 N11812897
#User defined exception(s) are employed for indicating error conditions

class InvalidInputException(Exception):
    def __str__(self):
        #the innput is not valid
        return 'Invalid input'