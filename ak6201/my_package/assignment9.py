
from income_dist import income_distribution
from exploration import exploratory_analysis
import sys
import logging
import pandas as pd
import numpy as np

def loop():
    loop_trial = 'y'
    
    try:
        country_by_region_data = pd.read_csv('countries.csv')
        gdp_by_year = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx')  # Loading the data
        cntry_cls = income_distribution() # Create a class for country class
        cntry_cls.set_Data(country_by_region_data, gdp_by_year) # To assign the data for the class variables
        
        print('The head of the transposed gdp_by_year data is :')
        print(cntry_cls.display_head())  # For question no 4 (display head)
        
        print('Instructions: \nPlease enter the year for which you want to see the graphical distribution of income per person across all countries in the world')
        print('Note: Enter years only between 1800 and 2012 (inclusive)')  #Instructions
        yr = input('>>') 
        
        while(yr != 'finish'):
            cntry_cls.check_valid_year(yr, 1)
            if cntry_cls.valid_input == 1:
                cntry_cls.all_countries_graph_by_year(yr)
            
            print('Enter another year (or finish to quit)')
            yr = input('>>')
            
        # After the user enters finish, Histogram and Boxplots for the years 2007 - 2012 is generated:
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        logging.info("Generating histograms and boxplots for 2007-2012")
        print('\nThe Histogram and Boxplots for the years 2007 - 2012 has been appended in the pdf file located in the same path')
        
        list_years = np.arange(2007,2013,1)
        explore = exploratory_analysis() # To create a class for exploration to access the histogram and boxplot functions
        
        for i in list_years:
            merged_data = cntry_cls.merge_by_year(i) # Get the merged data for a particular year using the function in country class and perform exploration
            explore.plt_Histogram(merged_data, i)
            explore.plt_Boxplot(merged_data, i)
            
    except KeyboardInterrupt:
        print("Keyboard Exit! Quitting..")
        sys.exit()

    
    
if __name__ == "__main__":
    try:
        loop()
    except EOFError:
        pass
