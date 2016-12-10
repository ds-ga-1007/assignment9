'''
Module of interaction functions:
1 InputTest()
2 WorldIncome_Iteraction()
3 RegionIncomeDisplay()
4 GlobalIncome_Display()

Created on Nov 28, 2016
Last Modified        : 
Version        : 1.0
@author: Nan Wu
@email: nw1045@nyu.edu
'''

from GlobalIncome import GlobalIncome,RegionIncome
from UserDefinedError import InputError,QuitProcess

def InputTest(year,YearList):
    '''
    Check and return Valid Input from user.
    Args:
        year: original input
        YearList: available input set
    Returns:
        year: tranform to int
    Raises:  
        InputError
        ValueError
    '''
    try:
        if (int(year) in YearList):
            return int(year)
        else:
            print("This year has no information. \nPlease try another in the available year list above.")
            raise InputError
    except ValueError:
        print('Invalid Input!')
        raise InputError
            
def WorldIncome_Interaction(ALLDATA):
    ''' 
    User Interaction for the first function of the project
    Args:
        ALLDATA: dataset 
    Returns:
        
    Raises:  
    
    '''
    print("The distribution of income per person across all countries in the world for the given year is provided.")
    print("Require for a graphically display by inputting a specific year.")
    print("Please check with all available years above.")
    print("You can get out from this session by a 'finish'.")
    print("You need to close the former figure to continue inputing.")
    year = input("Please input a Year (Example 1900):")
    while ((year !='finish') and (year !='quit')):
        try:
            year=InputTest(year, ALLDATA.income.index)
            ALLDATA.worldIncomeDistribution(int(year))
            year = input("Please input a Year (Example 1900):")
        except InputError:
            year = input("Please input a Year (Example 1900):")
    if year=='quit':
        raise QuitProcess
def RegionIncomeDisplay(ALLDATA,yearList):
    ''' 
    User Interaction for the second function of the project
    Args:
        ALLDATA: dataset
        yearList: reports of time interval  
    Returns:
        
    Raises:  
    
    '''
    print("Generating Income reports by region of 2007-2012...")
    for year in yearList:
        print("Reports of "+str(year))
        new_data = ALLDATA.merge_by_year(year)
        regionIncome = RegionIncome(new_data,year,ALLDATA.DataPath)
        regionIncome.GenerateReport()
    print("Finish and QUIT!")
        
def GlobalIncome_Display(DataPath):
    ''' 
    Main function
    Args:
        DataPath: path of the two dataset (please put your data in the same path)
    Returns:
        
    Raises:  
    
    '''
    ALLDATA = GlobalIncome(DataPath)
    ALLDATA.loadingData()
    ALLDATA.datatransform()
    ALLDATA.AvailableYears()
    WorldIncome_Interaction(ALLDATA)
    RegionIncomeDisplay(ALLDATA,range(2007,2013))
            
        
        
    
    