'''
Created on Dec 3, 2016

@author: Zahra KAdkhodaie
'''
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.text import Text

'''Load the datasets. These datasets must be in the same folder as the code.'''
countries = pd.read_csv('countries.csv')
income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx ')

'''transform the data set to have years as the rows and countries as the columns, 
then show the head of this data set when it is loaded.'''
income_rotated = income.T
income_rotated = income_rotated.drop('gdp pc test')
income_rotated.head()
income_rotated.columns = income['gdp pc test']
print(income_rotated.head())  


def visualize_income_year(year):
    '''This function graphically displays the distribution of income per person across all countries in the world for
      the given year with a bar chart. The bar chart has an slider and can be use in an interactive way. '''
    #prepare the data set to be used
    income_year = income_rotated.ix[year] 
    income_year = income_year.dropna()
    income_year.sort() 
    
    myfigure = plt.figure(figsize=(16, 8)) 
    myaxes = myfigure.add_subplot(1, 1, 1)  
    myfigure.subplots_adjust(bottom=0.3) #make room for x labels

    x_values = range(1, len(income_year)+1 )
    myaxes.bar(x_values, income_year.values , width =.5, edgecolor = 'green')
    
    myaxes.set_xticks([x + 0.25 for x in  x_values ])
    myaxes.set_xticklabels(income_year.index, size = 'small')
    plt.xticks(rotation=80)

    plt.title('Income per person by country in year ' + str(year))
    myfigure.text(.1,.1, 'Use the slider to explore the graph', color= 'red', size='large')
    
    myaxes.set_xlim(1, 30)
    
    Slider_axes = plt.axes([0.15, 0.03, 0.7, 0.03])
    myslider = Slider(Slider_axes, 'Slider', 0,  len(income_year)-30, valinit = 5)
    
    myslider.valtext.set_visible(False)
    
    def update(val):
        myaxes.axis([myslider.val, myslider.val + 30, 0, income_year.max()])
        myfigure.canvas.draw_idle()

    myslider.on_changed(update) 
    
    plt.show()


def merge_by_year(year):
    '''merges the countries and income data sets for any given year. 
    The result is a DataFrame with three columns titled Country, Region, and Income.'''
    if year not in income.columns:
        return ('No data for this year!')
    else: 
        smallData = income[['gdp pc test' , year]]
        smallData.columns = ['Country', 'Income']
        mergedData = smallData.merge(right = countries, how = 'inner', on= 'Country')
        return mergedData