import pandas as pd
#import plotly.graph_objs as go
from plotly import offline

df = pd.read_csv('https://raw.githubusercontent.com/yankev/test/master/life-expectancy-per-GDP-2007.csv')

americas = df[(df.continent=='Americas')]
europe = df[(df.continent=='Europe')]

trace_comp0 = {
    'type': 'scatter',
    'x': americas.gdp_percap,
    'y': americas.life_exp,
    'mode': 'markers',
    'marker': {
        'size': 12,
        'line': {'width': 1},
        'color': 'navy',
    },
    'name': 'Americas',
    'text': americas.country,
}

trace_comp1 = {
    'type': 'scatter',
    'x': europe.gdp_percap,
    'y': europe.life_exp,
    'mode': 'markers',
    'marker': {
        'size': 12,
        'line': {'width': 1},
        'color': 'red'
    },
    'name': 'Europe',
    'text': europe.country,
}

data_comp = [trace_comp0, trace_comp1]
layout_comp = {
    'title': 'Life Expectancy v. Per Capita GDP, 2007',
    'hovermode': 'closest',
    'xaxis': {
        'title': 'GDP per capita (2000 dollars)',
        'ticklen': 5,
        'zeroline': False,
        'gridwidth': 2,
    },
    'yaxis': {
        'title': 'Life Expectancy (year)',
        'ticklen': 5,
        'gridwidth': 2,
    },
}
fig_comp = {'data': data_comp, 'layout': layout_comp}
offline.plot(fig_comp, filename='pyguide_life.html')