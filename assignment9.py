from class_functions import *
countries = pd.read_csv('countries.csv')
income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx', index_col=0).transpose()
print(income.head())



while True:
    try:
        input_year = input('Please enter year from 1800 to 2012. Enter "finish" to exit the program')
        if input_year == 'finish':
            break
        input_year = int(input_year)
        income_distribution(input_year)
    except ValueError:
        print('Please enter a valid year between 1800 to 2012.')
    except KeyError:
        print('Please enter a valid year between 1800 to 2012.')
    except KeyboardInterrupt:
        break
    except EOFError:
        break

for year in range(2007, 2013):
    plot = Exploratory_Data_Analysis()
    plot.boxplots(year)
    plot.histogram(year)
