import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Open the filename.
filename = 'Projects/DataVisualization/DownloadingData/CSV_Format/data/world_fires_7_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Go through the header row and return the index.
    for index, column_header in enumerate(header_row):
        print(index, column_header)
