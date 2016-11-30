from function import *
from hist_box_class import hist_box
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def justify(year):
    #The function is used to justify if the input is valid
    flag=0;
    if(year.isdigit()==False):
        flag=1
    elif(int(year)<1800 or int(year)>2012):
        flag=1
    else:
        flag=0
    return flag


def main():
    #The program is used to plot the income histogram for the users' interested year
    #If the input is not valid, the program will output a warning and ask the user to input again until the input is correct or entering "finish"
    income=load_income('e:/income.xlsx')
    #Let the user input the interested year
    year=input("Please enter the year you are interested from 1800 to 2012. Quit the program by entering finish\n")
    flag=justify(year)
    #If the user do not input "finish", the program will continue asking user to input interested year
    while(year!="finish"):
        #If the input is not valid, the program will output a warning and ask the user to input again until the input is correct or entering "finish"
        while(flag==1):
            year=input("The last input is not valid. Please enter the year you are interested from 1800 to 2012. Quit the program by entering finish\n")
            flag=justify(year)
            if(year=="finish"):
                break
        #If the input is valid, the histgram and boxplot will be given and then let the user enter another year
        if(flag==0):
            hist_income(income,int(year))
            year=input("Please enter the year you are interested from 1800 to 2012. Quit the program by entering finish\n")
            flag=justify(year)
    for year in range(2007,2013):
        pic=hist_box(year)
        pic.figure()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard Interruption")