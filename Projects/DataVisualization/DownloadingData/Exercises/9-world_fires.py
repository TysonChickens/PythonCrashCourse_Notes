import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Open the filename.
# Limit the rows.
limit_data_rows = 20000
filename = 'Projects/DataVisualization/DownloadingData/CSV_Format/data/world_fires_7_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Go through the header row and return the index.
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Gather data for brightness, lats, lons, and dates.
    brightnesses, dates, lats, lons, hover_texts = [], [], [], [], []
    limit_data_row = 0
    for row in reader:
        brightness = float(row[2])
        brightnesses.append(brightness)
        date = datetime.strptime(row[5], '%Y-%m-%d')
        lat = lats.append(row[0])
        lon = lons.append(row[1])
        label = hover_texts.append(f"{date.strftime('%m-%d-%y')} - {brightness}")

        
        # Limit the data and stop the loop to prevent slow down.
        limit_data_row += 1
        if limit_data_row == limit_data_rows:
            break

# Map the fires.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [brightness/50 for brightness in brightnesses],
        'color': brightnesses,
        'colorscale': 'ylOrRd',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'},
    }
}]

my_layout = Layout(title='Global Fire Activity - 7 Days')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='Projects/DataVisualization/DownloadingData/CSV_Format/global_fires.html')