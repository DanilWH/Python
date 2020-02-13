import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/all_hour.json'
with open(filename) as f:
    eq_obj = json.load(f)

eq_dicts = eq_obj['features']
map_title = eq_obj['metadata']['title']

name_places, lons, lats, mags = [], [], [], []
for eq_dict in eq_dicts:
    name_places.append(eq_dict['properties']['place'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    mags.append(eq_dict['properties']['mag'])

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': name_places,
    'marker': {
        'size': [mag*8 for mag in mags],
        'reversescale': True,
        'color': mags,
        'colorscale': 'Viridis',
        'colorbar': {'title': 'Magnitudes'}
    }
}]

my_layout = Layout(title=map_title)
offline.plot({'data': data, 'layout': my_layout},
    filename='last_hour_earthquakes.html')