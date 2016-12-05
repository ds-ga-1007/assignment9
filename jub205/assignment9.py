"""
Created on Sat Dec 3 2016

@author: jinubak/jub205
@desc: This program loads countries and income data from csv and excel files
       then asks user to input a year between 1800 to 2012 and plots the 
       distribution of income across the world for that given year.
       When user inputs 'finish', it will plot boxplot and histogram of 
       income data by region from year 2007 to 2012.
"""
import GDPanalysis as gdp

def main():
    
    country_file = '../countries.csv'    
    countries = gdp.load_country_data(country_file)
    income_file = '../indicator gapminder gdp_per_capita_ppp.xlsx'
    income = gdp.load_gdp_data(income_file)
    
    print(income.head())
    
    ExitLoop = False
    
    while not ExitLoop:
        
        year_from_user = gdp.get_user_input()
        
        if year_from_user == 'finish':
            years = [str(i) for i in range(2007,2013)]
            print("Saving boxplot and histogram of income per person by region from 2007 to 2012\n")
            for year in years:
                merged_data = gdp.merge_by_year(year, countries, income)
                analysistool = gdp.IncomeAnalysis(merged_data,year)
                analysistool.plot_boxplot()
                analysistool.plot_histogram()
            print("Terminating the program")
            ExitLoop = True
            
        else:
            gdp.plot_income_distribution_by_year(income, year_from_user)
        
if __name__ == "__main__":
    
    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard interrupted, Terminating the program")
    
