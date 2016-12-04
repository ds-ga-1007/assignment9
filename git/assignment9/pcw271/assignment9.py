
# coding: utf-8

# In[ ]:




# In[ ]:




# In[2]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

countries = pd.read_csv('/Users/KateWu/git/assignment9/countries.csv',header=0)

#Q2
#income = pd.read_csv('/Users/KateWu/git/assignment9/indicator gapminder gdp_per_capita_ppp.csv') 
income = pd.read_excel('/Users/KateWu/git/assignment9/indicator gapminder gdp_per_capita_ppp.xlsx',header=0) 
#print(income)
trans_income = income.T
stack_income = income.stack()
#print(trans_income.head(5))
#print(stack_income.head(5))     #test the defference and result from transpose and stack
new_header=trans_income.ix[0]
#Q3
new_income=trans_income[1:]
a_new_income = new_income.rename(columns=new_header)
#print(a_new_income)

#Q4
def income_year(income,year):
    try:
        income = income.fillna(0)
        values = income.loc[year]
        sort_values = pd.Series.sort_values(values)
        plt.figure(num=None, figsize=(30, 60), dpi=100, facecolor='w', edgecolor='k')
        sort_values.plot.barh()
        plt.subplots_adjust(left=0.15)
        plt.show()
    except ValueError:
        print('Value error.')
    except (EOFError, KeyboardInterrupt):
        print('User Interrupt.')
    except:
        print('Unknown error.')

#income_year(a_new_income,2003)   

def group_by_region_and_country(income):
    try:
        merge_data = pd.merge(income,countries,left_on='gdp pc test',right_on='Country')  
        b = merge_data.groupby([merge_data.Region,merge_data.Country])
        return b
    except ValueError:
        print('Value error.')
    except (EOFError, KeyboardInterrupt):
        print('User Interrupt.')
    except:
        print('Unknown error.')

group_by_region_and_country=group_by_region_and_country(income)

def group_by_region(income):
    try:
        merge_data = pd.merge(income,countries,left_on='gdp pc test',right_on='Country')  
        b = merge_data.groupby([merge_data.Region])
        return b
    except ValueError:
        print('Value error.')
    except (EOFError, KeyboardInterrupt):
        print('User Interrupt.')
    except:
        print('Unknown error.')

group_by_region = group_by_region(income)

def select_year(group, year):
    try:
        b = group.sum()
        return b[year]
    except ValueError:
        print('Value error.')
    except (EOFError, KeyboardInterrupt):
        print('User Interrupt.')
    except:
        print('Unknown error.')

#Q5
def merge_by_year(year):
    try:
        merge_data = pd.merge(income,countries,left_on='gdp pc test',right_on='Country')  
        group_by_region_and_country = merge_data.groupby([merge_data.Region,merge_data.Country])
        set_year = group_by_region_and_country.sum()[year]
        print(set_year)
    except ValueError:
        print('Value error.')
    except (EOFError, KeyboardInterrupt):
        print('User Interrupt.')
    except:
        print('Unknown error.')
    

#print(merge_by_year(1981))


#Q6
class graph:
    
    def hist_by_region(group_by_region, year, region):
        select_region = group_by_region.get_group((region))
        select_region.index = select_region[select_region.columns[214]]
        select_region = select_region.ix[:,1:214]
        #print(select_region[year])
        #bins = np.linspace(-10, 10, 100)
        bins = np.linspace(math.ceil(min(select_region[year])),math.floor(max(select_region[year])), 20)
        hist = select_region[year].plot.hist(bins = bins, alpha=0.5) 
        #locs, labels = xticks()
        plt.xlim([-5000, 100000])
        plt.xlabel('Income')
        #plt.ylim([0, 10])
        #select_year = select_region[year]
        #hist = plt.hist(select_year,bins, alpha=0.5, label=year)
        plt.legend(loc='upper right')
        plt.title(region)
        return(hist)
    
    def boxplot_by_region(group_by_region, year, region):
        select_region = group_by_region.get_group((region))
        select_region.index = select_region[select_region.columns[214]]
        select_region = select_region.ix[:,1:214]
        #fig = ax.get_figure()
        select_year = select_region[year]
        boxplot = plt.boxplot(select_year)
        return(boxplot)

              
'''  
plt.figure(1,figsize=(20,10))
plt.subplot(121)
graph.hist_by_region(group_by_region,year_input,'AFRICA')
plt.subplot(122)
graph.boxplot_by_region(group_by_region,year_input,'AFRICA')
plt.savefig('/Users/KateWu/Desktop/PDB_HW9/Q8_AFRICA')

plt.figure(2,figsize=(20,10))
plt.subplot(221)
graph.hist_by_region(group_by_region,year_input,'ASIA')
plt.subplot(222)
graph.boxplot_by_region(group_by_region,year_input,'ASIA')
plt.savefig('/Users/KateWu/Desktop/PDB_HW9/Q8_ASIA')

plt.figure(3,figsize=(20,10))
plt.subplot(321)
graph.hist_by_region(group_by_region,year_input,'EUROPE')
plt.subplot(322)
graph.boxplot_by_region(group_by_region,year_input,'EUROPE')
plt.savefig('/Users/KateWu/Desktop/PDB_HW9/Q8_EUROPE')

plt.figure(3,figsize=(20,10))
plt.subplot(321)
graph.hist_by_region(group_by_region,year_input,'NORTH AMERICA')
plt.subplot(322)
graph.boxplot_by_region(group_by_region,year_input,'NORTH AMERICA')
plt.savefig('/Users/KateWu/Desktop/PDB_HW9/Q8_NORTH_AMERICA')

plt.figure(3,figsize=(20,10))
plt.subplot(321)
graph.hist_by_region(group_by_region,year_input,'OCEANIA')
plt.subplot(322)
graph.boxplot_by_region(group_by_region,year_input,'OCEANIA')
plt.savefig('/Users/KateWu/Desktop/PDB_HW9/Q8_OCEANIA')

plt.figure(3,figsize=(20,10))
plt.subplot(321)
graph.hist_by_region(group_by_region,year_input,'SOUTH AMERICA')
plt.subplot(322)
graph.boxplot_by_region(group_by_region,year_input,'SOUTH AMERICA')
plt.savefig('/Users/KateWu/Desktop/PDB_HW9/Q8_SOUTH_AMERICA')
'''

#Q7
def user_input_year(a_new_income):
   
    while True:
        try:
            year = input('Please enter the year: ')
            if year == 'finish':
                break
            else:
                int_year = int(year)
                income_year(a_new_income,int_year)
                plt.close()
        except ValueError:
            print('The input is invalid')
            continue
            
#user_input_year(a_new_income)   

#Q8
year_serial = list(range(2007,(2012)+1))

def hist_serial_years(year_serial,region,income_group_by_region):
    try:
        for i in year_serial:
            graph.hist_by_region(income_group_by_region,i,region)
            plt.savefig('/Users/KateWu/Desktop/PDB_HW9/Q8_{region}{i}'.format(region=region,i=i))
            plt.close()
    except ValueError:
        print('Value error.')
    except (EOFError, KeyboardInterrupt):
        print('User Interrupt.')
    except:
        print('Unknown error.')
        

'''
hist_serial_years(year_serial,'AFRICA',group_by_region)
hist_serial_years(year_serial,'ASIA',group_by_region)
hist_serial_years(year_serial,'EUROPE',group_by_region)
hist_serial_years(year_serial,'NORTH AMERICA',group_by_region)
hist_serial_years(year_serial,'OCEANIA',group_by_region)
hist_serial_years(year_serial,'SOUTH AMERICA',group_by_region)
'''    


# In[ ]:




# In[ ]:




# In[ ]:



