import csv
from get_indices import get_name, get_indices
from plotly.graph_objs import Scattergeo, Layout
from plotly.offline import offline

filename = 'C:\\Users\\HP\\Desktop\\getting ready\\PROJECTS\\data_visualization\\data\\world_fires_24h.csv'
f = open(filename)
reader = csv.reader(f)
header_row = next(reader)
lats, longs, brights, dates, powers = [],[],[],[],[]
for row in reader:
    lats.append(float(row[get_indices(header_row, 'latitude')]))
    longs.append(float(row[get_indices(header_row,'longitude')]))
    brights.append(float(row[get_indices(header_row,'brightness')]))
    dates.append(row[get_indices(header_row,'acq_date')])
    powers.append(float(row[get_indices(header_row,'frp')]))
    
f.close()
data = [{
    'type': 'scattergeo',
    'lon': longs,
    'lat': lats,
    'text' : dates, 
    'marker':{
        'size': [power/100 for power in powers if power>0],
        'color': [color/100 for color in brights],
        'colorscale': 'Inferno',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'}
    },
}]

layt = Layout(title = 'WORLD FIRES ON 18/08/2021 AND 19/08/2021.')
fig = {'data': data, 'layout': layt}
offline.plot(fig, filename='world_fires_18+19-08.html')