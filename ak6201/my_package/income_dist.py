import matplotlib.pyplot as plt

class income_distribution:
    valid_input = 1   # flag value to check whether input is valid or not
    
    def set_Data(self, country_by_region_data, gdp_by_year): #to assign the data to the class variables
        self.country_by_region_data = country_by_region_data
        self.gdp_by_year = gdp_by_year
        self.gdp_by_year = self.gdp_by_year.rename(columns={'gdp pc test': 'Country'}) #replace gdp pc test to Country <-- a better indicator
    
    def check_valid_year(self, year, to_print_or_not): # the second argument (to_print_or_not) is to print the error message only when the function is called. It is not printed when it is run for test cases
        self.valid_input = 1
        try:
            yr = int(year)
            if yr < 1800 or yr > 2012: # because the valid years are 1800-2012. if the user enters other than this, give him/her a warning
                if to_print_or_not == 1:
                    print('Please enter year between 1800 and 2012 (inclusive)')
                self.valid_input = 0
        except ValueError:
            self.valid_input = 0
            if to_print_or_not == 1:
                print("Invalid format for year")
                
    def display_head(self):  #function to display the head of transposed gdp data <--question no 4
        gdp_by_year_rot = self.gdp_by_year.T
        gdp_by_year_rot= gdp_by_year_rot.drop('Country')  # to remove the indices country column values and 
                                                          # replace the column values with the country values instead in the transpoed data
        gdp_by_year_rot.columns = self.gdp_by_year['Country']
        return gdp_by_year_rot.head()

        
    def all_countries_graph_by_year(self, year):  # to get the year from the user and display the distribution of the income data for all the countries 
        year = int(year) 
        inc_all_countries = self.gdp_by_year[year].dropna()
        inc_all_countries.plot(kind='hist')  # Histogram is a better representation as it approximates the distribution appropriately 
        plt.show()
        plt.xlabel('Income distribution for all the countries')
        plt.ylabel('Count')
        plt.title('The distribution of income for the year ' + str(year))
        
    def merge_by_year(self, year): # To merge the income data and the countries data for a given year 
        year = int(year)
        income_year = self.gdp_by_year
        income_year = income_year[['Country', year]] 
        income_year.columns= ['Country', 'Income'] #to replace the column name 'year' to income as a meaningful name
        data_merged = income_year.merge(right=self.country_by_region_data, how='inner', on='Country') #use the merge function on Country and perform inner join(to neglect the empty values)
        return data_merged
        
            
        