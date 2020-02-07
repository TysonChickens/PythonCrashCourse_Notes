# Use the pyplot function ylim() to set limits of the y-axis for better comparison of temp range.

import csv
from datetime import datetime

import matplotlib.pyplot as plt

def get_sitka_weather_data(filename, dates, highs, lows):
    """Get the highs and lows from data file."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')    
            try:
                high = int(row[5])
                low = int(row[6])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

def get_death_valley_weather_data(filename, dates, highs, lows):
    """Get the highs and lows from data file."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')    
            try:
                high = int(row[4])
                low = int(row[5])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

# Get weather data for Sitka.
dates, highs, lows = [], [], []
get_sitka_weather_data('Projects/DataVisualization/DownloadingData/data/sitka_weather_2018_simple.csv', dates, highs, lows)

# Sitka weather plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)

# Get weather data for Death Valley.
dates, highs, lows = [], [], []
get_death_valley_weather_data('Projects/DataVisualization/DownloadingData/data/death_valley_2018_simple.csv', dates, highs, lows)

# Add Death Valley to current plot.
plt.plot(dates, highs, c='red', alpha=0.3)
plt.plot(dates, lows, c='blue', alpha=0.3)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily High and Low Temperatures - 2018\nDeath Valley, CA & Sitka, AK"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.ylim(10, 150)

plt.show()