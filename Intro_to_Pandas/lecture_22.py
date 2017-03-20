import numpy as np
import pandas as pd

from pandas import Series, DataFrame

arr = np.array([[1,2,np.nan],[np.nan,3,4]])

dframe1 = DataFrame(arr,index=['A','B'],columns=['One','Two','Three'])

dframe1.sum() # sum of all columns

dframe1.sum(axis=1) # sum of all rows

dframe1.min() # find min value in each column
dframe1.idxmin() # find the index of the min value in each column

dframe1.cumsum() # cumulative sum

dframe1.describe() # provides summary statistics

###########

import pandas.io.data as pdweb

import datetime

stockList = ['CVX','XOM','BP']
prices = pdweb.get_data_yahoo(stockList, start=datetime.datetime(2010,1,1), end=datetime.datetime(2013,1,1))['Adj Close']

prices.head() # preview of the dataframe

volume = pdweb.get_data_yahoo(stockList,start=datetime.datetime(2010,1,1), end=datetime.datetime(2013,1,1))['Volume']

volume.head()

rets = prices.pct_change()

#Correlation fo the stocks
corr = rets.corr

prices.plot()

import seaborn as sns
import matplotlib.pyplot as plt

sns.corrplot(rets,annot=False,diag_names=False) # sns.corrplt seams to be specific to Jupiter Notebooks. 
