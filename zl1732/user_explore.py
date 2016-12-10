from hist_and_boxplot import *


'''
we import functions of ploting histogram and boxplot in this program
and will output the result and write to file in this class
'''
class user_explore():
    def __init__(self):
        return
    
    '''
    save the result to the pdf file
    save1: histogram of all the data, not by region
    save2: histogram by region
    save3: boxplot by region
    '''
    def save_plot(self,year):   
        fig_bp = plt.figure()
        ax = fig_bp.add_subplot(111)
        boxplot(year,ax)
        fig_bp.savefig("boxplot_"+str(year).zfill(4)+".pdf")
        
        fig_hist = plt.figure()
        ax = fig_hist.add_subplot(111)
        plot_hist_region(year,ax)
        fig_hist.savefig("hist_region_"+str(year).zfill(4)+".pdf")

        fig = plt.figure()
        plot_hist(year)
        fig.savefig("hist_all_"+str(year).zfill(4)+".pdf")