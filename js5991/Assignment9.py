'''
Created on Dec 3, 2016
This is the main module of assignment 9
@author: Jingyi Su js5991
@descriptions: This program asks user for a year and then display the graph of income per person across all countries in the world for the given year.
               The user will be ased the question until 'finished' is entered. 
               Then the program will generate boxplots and histograms for years 2007-2012 to display the income by region. 
'''
from income.load_display_data import plot_income
from income.income_by_region import income_by_region
import sys

if __name__ == '__main__':
    while True:
        try:
            inputstr=input('Please enter a year from 1800 to 2012 to see the income distribution of all nationals for that year. Enter "finished" if you want to end.')
            if (inputstr=='finished'):
                print("Finished the process")
                break
            year=int(inputstr)
            if(year>2012 or year<1800):
                raise ValueError('Invalid Input: please enter a year from 1800 to 2012.')
            plot_income(year)
        except ValueError as msg:
            print(msg)
        except KeyboardInterrupt:
            print ('Keyboard Interruption')
            sys.exit()
        except EOFError:
            print('EOFError')
            sys.exit()
    
    incomeByRegion=income_by_region()
    print ('Boxplots and histograms are saving in the Output folder')
    for year in range(2007, 2013):
        pathBoxPlot='Output/income_by_region '+str(year)+" boxplot.pdf"
        incomeByRegion.boxplot(year,pathBoxPlot)
        pathHistogram='Output/income_by_region '+str(year)+" histogram.pdf"
        incomeByRegion.histogram(year,pathHistogram)
    print ('All plots are saved in the output folder')
    
        
        
        