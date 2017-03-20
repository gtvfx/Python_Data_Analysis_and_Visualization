import numpy as np
import pandas as pd

from pandas import Series, DataFrame


ser1 = Series(np.arange(3),index=['a','b','c'])

ser1.drop('b') # remove an index

dframe1 = DataFrame(np.arange(9).reshape((3,3)),index=['SF','LA','NY'],columns=['pop','size','year'])

dframe1.drop('LA') # remove row
dframe1.drop('year',axis=1) # remove column
