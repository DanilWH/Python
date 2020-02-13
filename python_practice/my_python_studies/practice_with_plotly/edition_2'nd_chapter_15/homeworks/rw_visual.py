from plotly.graph_objs import Scatter, Layout
from plotly import offline
from random_walk import RandomWalk

rw = RandomWalk()
rw.make_steps()

each_point = list(range(1, rw.num_points+1))
data = [{
    'type': 'scatter',
    'x': rw.x_steps,
    'y': rw.y_steps,
    'mode': 'markers',
    'marker': {
        'color': each_point,
        'colorscale': 'Blues',
        'reversescale': True,
    },
}]

my_layout = Layout(title='Random Walk')

offline.plot({'data': data, 'layout':my_layout}, filename='rw_visual.html')