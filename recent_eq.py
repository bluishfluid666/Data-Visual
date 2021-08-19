import json
from json import encoder
from plotly.graph_objs import Layout, Scattergeo
from plotly.offline import offline

filename = 'data/eq_week32nd2021.json'
with open(filename, encoding='utf-8') as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
title = all_eq_data['metadata']['title'] 
longs = [eq_dict['geometry']['coordinates'][0] for eq_dict in all_eq_dicts]
lats = [eq_dict['geometry']['coordinates'][1] for eq_dict in all_eq_dicts]
mags = [eq_dict['properties']['mag'] for eq_dict in all_eq_dicts]
hovertexts = [eq_dict['properties']['title'] for eq_dict in all_eq_dicts]

data = [{
    'type': 'scattergeo',
    'lon': longs,
    'lat': lats,
    'text': hovertexts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Magma',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    }

}]

my_layout = Layout(title=title)
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'data/recent_eq.html')