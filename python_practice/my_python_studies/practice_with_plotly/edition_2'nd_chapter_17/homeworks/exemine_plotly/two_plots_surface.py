from plotly import tools
import numpy as np
from plotly import offline
import plotly.graph_objs as go

heatmap = go.Heatmap(
        z=[[1, 20, 30],
           [20, 1, 60],
           [30, 60, 1]],
           showscale=False
           )

y0 = np.random.randn(50)
y1 = np.random.randn(50) + 1

box_1 = go.Box(y=y0)
box_2 = go.Box(y=y1)
data = [heatmap, box_1, box_2]

fig = tools.make_subplots(rows=2, cols=2, specs=[[{}, {}], [{'colspan': 2},
    None]], subplot_titles=('First Subplot', 'Second Subplot', 'Third Subplot'))

fig.append_trace(box_1, 1, 1)
fig.append_trace(box_2, 1, 2)
fig.append_trace(heatmap, 2, 1)

fig['layout'].update(height=600, width=600, title='i <3 subplots')

fig.data[1].yaxis = 'y1'
fig.data[1].xaxis = 'x1'

fig.layout.xaxis1.domain = [0.0, 1]

offline.plot(fig, filename='box_heatmap1.html')