from plotly import offline
import numpy as np

x = np.arange(1, 3.2, 0.2)
y = 6 * np.sin(x)

trace1 = {
    'type': 'scatter',
    'x': [1, 2, 3],
    'y': [4, 5, 6],
    'marker': {'color': 'red', 'symbol': 104, 'size': 10},
    'mode': 'markers+lines',
    'text': ['one', 'two', 'three'],
    'name': '1st Trace',
}

trace2 = {
    'type': 'scatter',
    'x': x,
    'y': y,
    'marker': {'color': 'blue', 'symbol': 'star', 'size': 10},
    'mode': 'markers',
    'name': '2nd trace',
}

layout = {
    'title': 'First Plot',
    'xaxis': {'title': 'x1'},
    'yaxis': {'title': 'x2'},
    'annotations': [{
        'text': 'Highest Point',
        'x': 3,
        'y': 6,
    }],
    'shapes': [
        # 1st highlight during Feb 4 - Feb 6
        {
            'type': 'rect',
            # x-reference is assigned to the x-values
            'xref': 'x',
            # y-reference is assigned to the plot paper [0, 1]
            'yref': 'y',
            'x0': 1,
            'y0': 0,
            'x1': 2,
            'y1': 7,
            'fillcolor': '#b3b3b3',
            'opacity': 0.2,
            'line': {
                'width': 0,
            }
        }]
}

data = [trace1, trace2]
plot2 = offline.plot({'data': data, 'layout':layout}, filename='pyguide.html')
