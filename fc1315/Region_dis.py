'''
Created on Dec 3, 2016
@author: Fanglin Chen
'''
class Region_dis():
    '''
    This class uses histograms and boxplots to graphically explore 
    the distribution of the income per person by region for a given year.
    '''
    
    def histogram(self, data):
        return data.hist(column = 'Income', by = 'Region', xlabelsize = 11, ylabelsize = 11, sharex = True)
    
    def boxplot(self, data):
        return data.boxplot(column = 'Income', by = 'Region')
    

   
class InputError(Exception):
    '''
    Exception raised for errors in the input.
    '''
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message