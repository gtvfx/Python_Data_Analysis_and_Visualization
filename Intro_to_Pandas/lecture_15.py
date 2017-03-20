import numpy as np
import pandas as pd

from pandas import Series, DataFrame

import webbrowser

website = 'https://en.wikipedia.org/wiki/NFL_win%E2%80%93loss_records'
webbrowser.open(website)

nfl_frame = pd.read_clipboard()

nfl_frame.columns
nfl_frame.Rank
nfl_frame.Team

nfl_frame['First Season']


DataFrame(nfl_frame, columns=['Team', 'First Season', 'Total Games', 'Stadium'])


nfl_frame.head()
nfl_frame.head(3)

nfl_frame.tail()
nfl_frame.tail(2)

nfl_frame.ix[3]

nfl_frame['Stadium'] = "Levi's Stadium"

nfl_frame['Stadium'] = np.arange(5)
nfl_frame

stadiums = Series(["Levi's Stadium", "AT&T Stadium"], index[4,0])
stadiums


nfl_frame['Stadium'] = stadiums

del nfl_frame['Stadium']
nfl_frame


data = {'City':['SF','LA','NYC'], 'Population':[837000,3880000,8400000]}

city_frame = DataFrame(data)
city_frame
