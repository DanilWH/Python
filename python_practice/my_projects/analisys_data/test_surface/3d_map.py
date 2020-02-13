import csv
import requests as rs
import pandas as pd

import plotly.graph_objs as go
from plotly import offline

url = 'https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv'
relief_list = pd.read_csv(url).as_matrix()

data = [{
    'type': 'surface',
    'z': relief_list,
    'colorscale': 'Viridis'
}]
my_layout = go.Layout(title='IDN')
offline.plot({'data': data, 'layout': my_layout}, filename='s.html')