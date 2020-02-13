import plotly.graph_objs as go
from plotly import offline
"""
trace1 = {
    'type': 'scatter',
    'marker': {'color': 'blue'},
}
"""
trace1 = go.Scatter(marker=dict(color='blue'))
data = [trace1]
layout = go.Layout(title='HUY')

trace1.update(dict(x=[1, 2, 3], y=[4, 5, 6],
    marker=dict(symbol='star', size=10)))
offline.plot({'data': data, 'layout': layout}, filename='proba.html')