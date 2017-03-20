import numpy as np
import pandas as pd
from pandas import Series, DataFrame

obj = Series([3,6,9,12])


ww2_cas = Series([8700000, 4300000, 3000000, 2100000, 400000],index=['USSR', 'Germany', 'China', 'Japan', 'USA'])

ww2_cas['USA']

#Check which countries had cas greater than 4 mil

ww2_cas[ww2_cas > 4000000]

if 'USSR' in ww2_cas: print 'Yes'

ww2_dict = ww2_cas.to_dict()

ww2_series = Series(ww2_dict)

####

countries = ['China', 'Germany', 'Japan', 'USA', 'USSR', 'Argentina']
obj2 = Series(ww2_dict, index=countries)

pd.isnull(obj2)
pd.notnull(obj2)

###

ww2_series + obj2

obj2.name = "World War 2 Cacualties"
print obj2

obj2.index.name = "Countries"
