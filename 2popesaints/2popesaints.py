# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd
from pandas.tseries.resample import TimeGrouper
from pandas.tseries.offsets import DateOffset


dataset = pd.read_csv('2pope.csv')
dataset['created_at'] = pd.to_datetime(pd.Series(dataset['created_at']))
dataset.set_index('created_at', drop=False, inplace=True)
dataset.index = dataset.index.tz_localize('GMT').tz_convert('CET')
dataset.index = dataset.index - DateOffset(hours = 12)
dataset.head()

# <codecell>

dataset.describe()

# <codecell>

# created_at timeseries is in a per minute minute format.
dataset1m = dataset['created_at'].resample('1t', how='count')
dataset1m.head()

# <codecell>

avg = dataset1m.mean()
print "average amount of tweets per minute ", avg

# <codecell>

import vincent

vincent.core.initialize_notebook()
area = vincent.Area(dataset1m)
area.colors(brew='Spectral')
area.display()

# <codecell>

# most used devices.
dataset.source.value_counts()[:15]

# <codecell>

geo = dataset.geo
geo = geo[geo.notnull()]
geo.head()

# <codecell>

import json
coordinates = []

for g in geo:
    coordinates.append(json.loads(g)['coordinates'])

# <codecell>

# plotting the map of twitts
import folium

#Simple Markers
wmap = folium.Map(location=[32.4942772,-34.505193], zoom_start=2)
for c in coordinates:
    wmap.simple_marker(c, popup='twitt')

wmap.create_map(path='2pop_map.html')

# <codecell>

from IPython.display import IFrame
# IFrame('file:///Users/uolter/src/pycode/mining_social_web/2popesaints/2pop_map.html', width=750, height=350)
IFrame('http://localhost:8000/2pop_map.html', width=800, height=950)

# <codecell>

# language detected
import matplotlib.pyplot as plt
from pandas import Series

lang = [('english', 6738), ('spanish', 6663), (None, 4700),
        ('italian', 2236), ('french', 1528), ('portuguese', 720), ('hungarian', 412), 
        ('swedish', 264), ('german', 251), ('danish', 198), ('dutch', 96), ('finnish', 47), 
        ('norwegian', 37), ('russian', 8), ('turkish', 4)]



tot = [l[1] for l in lang]
index = [l[0] for l in lang]

lang_series = Series(tot, index=index )

# make a histogram

Series.plot(lang_series, kind='bar', 
     title='2 Pope Saints tweets.'
     )

plt.xlabel('languages')
plt.ylabel('count')

# <codecell>


# <codecell>


# <codecell>


