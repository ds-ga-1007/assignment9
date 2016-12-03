# -*- coding: utf-8 -*-

'''

Author: Eduardo Fierro Farah 
NetID: eff254 

Assignment 9 for Programming for Data Science
Professor: Greg Watson

Purpose: 
This program uses data form gapminder to describe the distribution of income by year and by region 

'''

import Utils as ut
import time

countries = ut.importMyCsv("countries")
income = ut.importMyExcel("indicator gapminder gdp_per_capita_ppp") 
income = ut.stackUnstack(income)

print("Here are the first 5 rows of your dataset")
time.sleep(1)
print(income.head()) 
time.sleep(2)

finish = None
while finish is None:
    print("You can type 'finish' if you're done")
    usersYear = input("Please input a year to test so I can show you the distribution of income for that year: ")
    if usersYear == "finish":
        finish = True
    else:
        try: 
            usersYear = ut.stringToNumber(usersYear)
            if ut.TestIfInIndex(usersYear, income):
                ut.incomePerYear(income, usersYear)
            else: 
                print("Sorry! That year is not in our data base. \n \n")               
        except ut.numberNotANumber:
            print("Sorry, I couldn't recognize that number. Please try again \n \n")
            
print("...")
print("I am generating some plots you can check out in your local directory.... ")
print("...")
for year in range(2007, 2013):
    ut.exploreByRegion(year, income, countries).histograms()
    ut.exploreByRegion(year, income, countries).boxPlot()
    if year == 2010:
        print("Almost there") 
        print("...")
print("...")
print("Done!!!")
print("...")
print("...")
print("...")
print("Goodbye")

