import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_1_day_recent_version.csv'
with open(filename) as f:
    data_obj = csv.reader(f)
    headers = next(data_obj)

    date = next(data_obj)[5]
    lons, lats, brs_texts, brs_val = [], [], [], []
    for row in data_obj:
        lons.append(float(row[1]))
        lats.append(float(row[0]))
        brs_texts.append(f'Brightness-{row[2]}')
        brs_val.append(float(row[2]))

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': brs_texts,
    'marker': {
        'size': [br/100 for br in brs_val],
        'color': brs_val,
        'colorscale': 'Reds',
        'colorbar': {'title': 'Brightness of fire'}
    }
}]

my_layout = Layout(title=f'Fires by {date}')
offline.plot({'data': data, 'layout': my_layout}, filename='world_fires.html')