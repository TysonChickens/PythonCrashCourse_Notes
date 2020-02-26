import csv
from datetime import datetime

import matplotlib.pyplot as plt


def get_weather_data(filename, dates, highs, lows, name):
    """Get the highs and lows from data file."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        print(header_row)

        # Pull the indexes of the headers from the header row.
        date_index = header_row.index('DATE')
        high_index = header_row.index('TMAX')
        low_index = header_row.index('TMIN')
        name_index = header_row.index('NAME')
            
        # Grab from index dates, highs, lows = [], [], []
        for row in reader:
            # Grab current date and format it.
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')    
            try:
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
            # Grab the station name.
            if not name:
                names = row[name_index]
                name.append(names)
                print(name)


# Get weather data for San Francisco.
dates, highs, lows = [], [], []
name = []
get_weather_data('Projects/DataVisualization/DownloadingData/data/san_francisco_weather_2018.csv', dates, highs, lows, name)


# San Francisco weather plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)


# Format plot.
title = f"Daily High and Low Temperatures - 2018\n{name}"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.ylim(10, 100)

plt.show()