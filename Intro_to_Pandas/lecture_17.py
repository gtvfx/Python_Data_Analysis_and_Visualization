import numpy as np
import pandas as pd

from pandas import Series, DataFrame

from numpy.random import randn

ser1 = Series([1,2,3,4],index['A','B','C','D'])
ser1

ser2 = ser1.reindex(['A','B','C','D','E','F'])
ser2.reindex(['A','B','C','D','E','F','G'],fill_value=0)

ser3 = Series(['USA','Mexico','Canada'],index[0,5,10])
ser3

ranger = range(15)
ser3.reindex(ranger,method='ffill')
ser3

dframe = DataFrame(randn(25).reshape((5,5)),index=['A','B','D','E','F'],columns=['col1','col2','col3','col4','col5'])
dframe

dframe2 = dframe.reindex(['A','B','C','D','E','F'])
dframe2

new_columns = ['col1','col2','col3','col4','col5','col6']
dframe2.reindex(columns=new_columns)

dframe

dframe.ix[['A','B','C','D','E','F'],new_columns] # reindex columns and frames at the same time
