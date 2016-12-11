from functions import *
from module import *

for i in range(2007,2013,1):
    data = merge_by_year(i)
    graph = tool(i, data)
    graph.histogram()

for i in range(2007,2013,1):
    data = merge_by_year(i)
    graph = tool(i, data)
    graph.boxplot()