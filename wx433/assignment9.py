import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib
import sys

from IncomeAnalysisToolKit import *

while True:
	result_check = 0
	country_path = input('Please enter the path of your country information table.\n')
	

	try:
		country_table = pd.read_csv(country_path,index_col = 0, header = 0)	
		result_check += 1	
	except FileNotFoundError:
		print("Wrong Path")
	except:
		print('Invalid Source')

	income_path = input('Please enter the path of your income information table.\n')

	try:
		income_table = pd.read_excel(income_path,index_col = 0, header = 0).transpose()
		result_check += 1
	except FileNotFoundError:
		print("Wrong Path")
	except:
		print('Invalid Source')

	if result_check == 2:
		print("Tables are successfully created.")
		break

target = IncomeAnalysisToolKit(country_table, income_table)


while True:
	year1_input = input("Please give a target year to check the global income overview. (Type 'finish' to exit)\n")

	if year1_input.lower() == 'finish':
		break

	else:
		try:
			year1 = int(year1_input)
			try:	
				target.income_per_person(year1)
			except:
				print('Invalid Input.\n')
		except:
			print('Invalid Input.\n')


while True:
	year2_input = input("Please give a target year to check income information by region. (Type 'finish' to exit)\n")

	if year2_input.lower() == 'finish':
		break

	else:
		try:
			year2 = int(year2_input)
			try:	
				target.income_cross_region(year2)
			except:
				print('Invalid Input1.\n')
		except:
			print('Invalid Input2.\n')



if __name__ == '__main__':
    pass

