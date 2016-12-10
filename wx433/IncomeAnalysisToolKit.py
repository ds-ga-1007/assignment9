import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib



class IncomeAnalysisToolKit():

	def __init__(self, Country_df, Income_df):
		self.Country_df = Country_df
		self.Income_df = Income_df

	def print_tables(self):

		print(self.Country_df)
		print(self.Income_df)


	def income_per_person(self, year):
	    fig = plt.figure()
	    chosen_year = self.Income_df.ix[year]
	    chosen_year.hist()
	    plt.xlabel('Counts of Countries')
	    plt.ylabel('Income per Person')
	    plt.grid()
	    plt.title('The Distribution of Income per Person for %d' % year)
	    pdf_file = PdfPages('Income_Distribution_{:04d}.pdf'.format(year))
	    plt.savefig(pdf_file, format = 'pdf')
	    pdf_file.close()

	def merge_by_year(self, year):
	    income_info=pd.DataFrame(self.Income_df.loc[year])
	    ans = pd.merge(self.Country_df, income_info, right_index = True, left_index = True)
	    ans['Country'] = ans.index
	    ans.reset_index(drop = True,inplace=True)
	    ans.rename(columns = {year:'Income'}, inplace=True)
	    ans = ans[['Country', 'Region', 'Income']]
	    ans
	    return ans

	def income_cross_region(self, year):
	    data = self.merge_by_year(year)
	    matplotlib.rc('font', size=6)
	    matplotlib.rc('axes', titlesize=8)
	    pdf_file_hist = PdfPages('Income_Histogram_{0:04d}.pdf'.format(year))
	    pdf_file_box = PdfPages('Income_Boxplot_{0:04d}.pdf'.format(year))
	    fig_1 = plt.figure()
	    plt.title('The Boxplots of Income per Person in {0:04d} by Region'.format(year))
	    data.boxplot(column ='Income', by = 'Region')	    
	    plt.savefig(pdf_file_hist, format = 'pdf')
	    fig_2 = plt.figure()
	    plt.title('The Distribution of Income per Person in {0:04d} by Region'.format(year))
	    data['Income'].hist(by=data['Region'])
	    plt.savefig(pdf_file_box, format = 'pdf')
	    pdf_file_hist.close()
	    pdf_file_box.close()






