'''
Created on Dec 2, 2016

Functions to be used in the main program.

@author: ShashaLin
'''
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.text import Text
import pandas as pd
import numpy as np

def plot_year(year, income):
    
    plt.close()
    fig = plt.figure(figsize=(12, 8), dpi=80, facecolor='w', edgecolor='k')
    ax = fig.add_subplot(1, 1, 1)
    bar_color = 'lightskyblue'
    bar_height = income.loc[1901].values
    bar_width = .9
    bar_x = range(1, income.shape[1]+1)
    bar = ax.bar(bar_x, bar_height, color = bar_color, width = bar_width, edgecolor = 'none')
    
    ax.set_xticks([x + bar_width/2 for x in  bar_x ])
    ax.set_xticklabels(income.columns, size = 'x-small')
    plt.title('Per capita income by country in {}'.format(1901))
    ax.text(6, 6000, 'Drag the slider below to see country details', fontweight = 'bold', color = 'b', 
            horizontalalignment='center', size = 'large')
    
    ax.set_xlim(1, 10)
    
    axSlider = plt.axes([0.15, 0.03, 0.7, 0.03])
    slider = Slider(axSlider, 'Slider', 0,  90.0, valinit = 3)
    
    slider.valtext.set_visible(False)
    
    def update(val):
        ax.axis([slider.val, slider.val + 10, 0, income.loc[1901].max()])
        fig.canvas.draw_idle()

    slider.on_changed(update) 
    
    plt.show()
    
def merge_by_year(year, income, countries):
    
    commonCountries = list(income.columns) and list(countries.Country)
    countriesCommon = [row for row in list(countries.index) if countries.iloc[row, 0] in commonCountries ]
    
    countriesModified = countries.set_index(countries.Country).T
    
    yeardata = countriesModified[countriesCommon].append(income.loc[year, commonCountries])
    
    return yeardata

class Region():
    def __init__(self, year, df_year):
        hist_fig, hist_axes = plt.subplots(2, 3, figsize=(12, 8), dpi=80, facecolor='w', edgecolor='k')
        
        box_list = []
        for counter, region in enumerate(df_year.loc['Region'].unique()):
            df_region = pd.DataFrame([df_year.loc[:, i] for i in df_year.columns if df_year.loc['Region', i] == region])
            box_list.append(df_region.loc[:, year].dropna().values)
            
            hist_axes[counter//3-1, counter%3 -1].hist(df_region.loc[:, year].dropna().values, bins = 10, facecolor = 'green')
            hist_axes[counter//3-1, counter%3 -1].set_title('{}'.format(region), size = 'small')
            for tick in hist_axes[counter//3-1, counter%3 -1].xaxis.get_major_ticks():
                tick.label.set_fontsize(5.5) 
        hist_fig.savefig('histogram of {}.pdf'.format(year))
        plt.subplots_adjust(wspace = .2, hspace = .2)
        plt.suptitle('{} per capita income distribution'.format(year), size = 'medium')
        plt.show()
        
        plt.figure(figsize=(12, 8), dpi=80, facecolor='w', edgecolor='k')
        plt.boxplot(box_list)
        plt.xticks(np.arange(1, 7), df_year.loc['Region'].unique())   
        plt.ylim(0, 55000)      
        plt.title('boxplot of income by region for {}'.format(year))
        plt.savefig('boxplot of {}.pdf'.format(year))
        plt.show()