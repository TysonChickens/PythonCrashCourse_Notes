# Collect rainfall data for Sitka from PRCP header.
import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'Projects/DataVisualization/DownloadingData/data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get dates and precipitation from file.
    dates, rainfall = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        precipitation = float(row[3])
        dates.append(current_date)
        rainfall.append(precipitation)

# Plot the rainfall for each day of 2018.
plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.plot(dates, rainfall, c='blue')

# Format plot with title.
plt.title("2018 Rainfall - Sitka, AK", fontsize=24)
plt.xlabel('', fontsize=20)
fig.autofmt_xdate()
plt.ylabel("Amount of Precipitation (inches)", fontsize=14)
plt.bar(dates, rainfall, width=3, color='blue')

plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()