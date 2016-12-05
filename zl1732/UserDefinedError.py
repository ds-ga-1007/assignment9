
'''
this class define a type of error
that input is not an integar
'''
class NotInterror(Exception):
    def __init__(self, arg):
        self.args = arg

'''
this class define a type of error
that input is not in the given range
'''
class OutofRangeError(Exception):
    def __init__(self, args, min, max):
        self.args = args
        self.min = min
        self.max = max
        
