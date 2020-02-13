import random

import plotly.graph_objs as go
from plotly import offline

data = [
{
    'type': 'mesh3d',
    'x': [random.randint(0, 100) for num in range(70)],
    'y': [random.randint(0, 100) for num in range(70)],
    'z': [random.randint(0, 100) for num in range(70)],
    'color': 'pink',
    #'opacity': 0.5,
},
{
    'type': 'mesh3d',
    'x': [random.randint(0, 50) for num in range(70)],
    'y': [random.randint(0, 50) for num in range(70)],
    'z': [random.randint(0, 50) for num in range(70)],
    'color': 'yellow',
    'opacity': 0.5,
}
]
layout = {
    'title': 'Mesh3D',
}
offline.plot({'data': data, 'layout':layout}, filename='mesh.html')