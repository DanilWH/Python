import plotly.graph_objs as go
from plotly import offline

from point_density import PointDensity

pd = PointDensity()
pd.get_point()

data = [{
    'type': 'scatter3d',
    'x': pd.x_point,
    'y': pd.y_point,
    'z': pd.z_point,
    'mode': 'markers',
    'marker': {
        'size': 4
    }
}]
my_layout = {
    'title': 'Point Density',
}

offline.plot({'data': data, 'layout': my_layout},
        filename='point_density.html')