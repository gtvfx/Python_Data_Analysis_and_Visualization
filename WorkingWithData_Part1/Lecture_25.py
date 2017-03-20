import sys

import numpy as np
import pandas as pd

from pandas import Series, DataFrame


dframe = pd.read_csv('lec25.csv')

dframe = pd.read_csv('lec25.csv', header = None)

dframe = pd.read_table('lec25.csv',sep=',',header=None)

dframe = pd.read_csv('lec25.csv',header=None,nrows=2)


# write out
dframe.to_csv('mytextdata_out.csv')

dframe.to_csv(sys.stdout, sep='_')
