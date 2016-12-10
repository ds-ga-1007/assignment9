'''This program first loads two datasets ("countries" and "income"). It then prints
a preview of the transpose of the "income" data frame, with yearly GDP per Capita as the rows
and countries as the columns. The program then allows the user to enter a year; once the year
is entered, the program will display a histogram of GDP per Capita across all countries in the
world for that given year. The program continues to ask the user to input a year; the user must
type in the word 'finish' to break the loop. Finally, the program generates histograms and boxplots
illustrating the distribution of GDP for each region (Africa, Asia, Europe, North America, Oceania,
and South America) for each year between 2007 and 2012. 


Author: Brenton Arnaboldi (ba1303)
'''

from functions_and_classes import *

countries = pd.read_csv('/Users/Brenton/assignment9/countries.csv')
income = pd.read_excel('/Users/Brenton/assignment9/indicator gapminder gdp_per_capita_ppp.xlsx', index_col = 'gdp pc test')

print(income.transpose().head())

while True:
        response = input('Please enter a year. Type "finish" if you are done: ')
        if response == 'finish':
            break
        else:
            try:
                year = YEAR(int(response)).year_value
                display_income_distribution(year, income)
                print('Must close display for the program to continue. If you want to refer to the histogram later, the plot will be saved on your local system.')
                plt.show()
            except:
                print('Please enter a four-digit integer between 1800 and 2012')
                 
years = range(2007, 2013)
for year in years:
    annual_data = merge_by_year(year, income, countries)
    Graph('Income', 'Region', year, annual_data).create_histograms()
    Graph('Income', 'Region', year, annual_data).create_boxplots()   
