import plotly.graph_objs as go
from plotly import offline

from random_walk import RandomWalk3D

rw = RandomWalk3D()
rw.random_steps()

range_points = list(range(1, rw.num_points+1))
data = [{
    'type': 'scatter3d',
    'x': rw.x_steps,
    'y': rw.y_steps,
    'z': rw.z_steps,
    'mode': 'markers',
    'marker': {
        'color': range_points,
        'colorscale': 'Blues',
        'reversescale': True,
    }
}]

my_latout = go.Layout(title='Random Walk 3D')
offline.plot({'data': data, 'layout': my_latout}, filename='rw_3Dvisual.html')