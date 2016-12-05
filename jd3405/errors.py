# Solution for DS-GA 1007 Assignment#9
# Author: Jiaming Dong (jd3405@nyu.edu)
# NYU Center for Data Science


class InvalidInputException(Exception):
    def __str__(self):
        """return the error string"""
        return "Input is invalid"
