# Downloading Data

Downloading data sets from online sources and creating working visualizations of that data. Data is stored in two common formats, CSV and JSON. Python's `csv` module can process weather data stored in the CSV (comma-separated values) format and analyze high and low temperatures over time in two different locations. Then use Matplotlib to generate a chart based on downloaded data to display variations in temperature in two dissimilar environments: Sitka, Alaska, and Death Valley, California.

## The CSV File Format

A simple way to store data in a text file is to write the data as a series of values separated by commas, which is called ***comma-separated values***.

We begin with a small set of weather data of CSV-formatted to extract values from the data. An example of weather data from the file:

``` markdown
"USW00025333","SITKA AIRPORT, AK US","2018-03-15","0.00",,"45","36"
```

### Parsing the CSV File Headers

Python's `csv` module in the standard library parses the lines in a CSV files and allows us to quickly extract the values we are interested in. We can start by examining the first line of the file containing a series of headers for the data to tell us what kind of information it holds:

sitka_highs.py

``` python
import csv

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
```

1. After importing the `csv` module, we assign the name of the file to *filename*. Open up the file and assign the resulting file object to *f*.

2. Call `csv.reader()` and pass it the file object as an argument to create a reader object associated with that file. We assign the reader object to *reader*.

3. The csv module contains a `next()` function, which returns the next line in the file when passed the reader object. We call `next()` only once to get the first line of the file, which contains the headers. We store that data in *header_row* contains weather-related headers what information each line of data holds:

``` markdown
['STATION', 'NAME', 'DATE', 'PRCP', 'TAVG', 'TMAX', 'TMIN']
```

The `reader` object processes the first line of comma-separated values in the file and stores each as an item in a list. The position of each header tells us where the values are in each line and the description of them. The data we want right now is the date, the high temperature (TMAX), and the low temperature (TMIN). This is a simple data set of weather information of precipitation. Other weather data set can include a number of other measurements relating to wind speed, direction, and more detailed precipitation data.

### Printing the Headers and Their Positions

To make it easier to understand the file header data, we print each header and its position in the list:

sitka_highs.py

``` python
--snip--
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)
```

The `enumerate()` function returns both the index of each item and the value of each item as loop through the list. The line `print(header_row)` is removed in favor of more detailed version.

``` markdown
0 STATION
1 NAME
2 DATE
3 PRCP
4 TAVG
5 TMAX
6 TMIN
```

We see here the dates and their high temperatures are stored in columns 2 and 5. We only want to process each row of data and extract the values with the indexes of 2 and 5.

### Extracting and Reading Data

We know which columns of data we need, so we can extract the high temperature for each day:

sitka_highs.py

``` python
--snip--
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get high temperatures from this file.
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

print(highs)
```

1. Make an empty list called *highs*.

2. Loop through the remaining rows in the file. The `reader` object continues from where it left off in the CSV file and automatically returns each line followings its current position. The header loop has already been processed, and the loop begins at the second line to pull each line of data from index 5 (header for *TMAX*).

3. Use the `int()` function to convert the data, which is stored as a string, to a numerical format to use it. Then append the value to *highs*.

Here is the data:

``` markdown
[48, 48, 46, 42, 46, 44, 39, 36, 34, 28, 34, 41, 53, 63, 60, 54, 47, 46, 42, 45, 43, 41, 41, 40, 40, 41, 39, 40, 40, 39, 36, 35, 35, 34, 42, 41, 39, 42, 39, 37, 37, 40, 43, 41, 40, 38, 36, 37, 39, 39, 38, 41, 42, 41, 39, 38, 42, 39, 40, 35, 40, 41, 40, 39, 39, 40, 39, 42, 43, 44, 54, 58, 54, 45, 45, 45, 43, 41, 41, 42, 46, 42, 42, 41, 42, 43, 43, 46, 45, 43, 45, 41, 43, 45, 52, 51, 59, 52, 54, 57, 58, 51, 51, 48, 50, 49, 46, 46, 45, 45, 47, 47, 45, 46, 45, 45, 46, 47, 46, 44, 44, 47, 45, 48, 50, 56, 53, 51, 56, 52, 48, 49, 54, 45, 50, 51, 57, 52, 50, 52, 53, 52, 55, 52, 50, 52, 51, 50, 54, 53, 54, 58, 53, 57, 52, 63, 57, 59, 59, 60, 53, 51, 63, 56, 54, 60, 57, 54, 62, 67, 62, 57, 60, 57, 61, 60, 55, 56, 61, 57, 57, 62, 58, 70, 70, 67, 59, 58, 62, 66, 59, 56, 63, 65, 58, 56, 59, 64, 60, 60, 61, 65, 65, 63, 59, 64, 65, 68, 66, 64, 67, 65, 66, 59, 67, 73, 72, 64, 62, 61, 61, 63, 65, 62, 59, 61, 60, 63, 66, 63, 67, 65, 63, 59, 60, 58, 58, 63, 59, 61, 62, 61, 61, 57, 63, 62, 65, 67, 64, 65, 68, 66, 71, 69, 67, 61, 65, 62, 59, 60, 64, 63, 58, 64, 56, 56, 56, 57, 57, 57, 61, 64, 63, 66, 56, 54, 54, 57, 52, 53, 56, 54, 53, 52, 54, 56, 57, 60, 59, 55, 55, 56, 54, 56, 61, 61, 55, 55, 51, 54, 54, 55, 51, 47, 49, 45, 50, 48, 47, 46, 50, 51, 50, 47, 50, 54, 53, 49, 48, 48, 54, 52, 52, 51, 46, 47, 44, 48, 54, 53, 47, 45, 43, 39, 36, 39, 39, 41, 41, 44, 48, 52, 50, 45, 46, 43, 46, 49, 48, 48, 43, 39, 41, 44, 43, 41, 44, 46, 47, 44, 38, 42, 48]
```

The high temperature for each date and stored each value in a list.

### Plotting Data in a Temperature Chart

Create a simple plot of the daily highs using Matplotlib to visualize the temperature data:

sitka_highs.py

``` python
import csv

import matplotlib.pyplot as plt

filename = 'Projects/DataVisualization/DownloadingData/data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    --snip--

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# Format plot.
plt.title("Daily High Temperatures, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
```

1. Pass the list of highs to `plot()` and pass `c='red'` to plot the points in red. (The highs in red and the lows in blue).

2. Specify formatting details, such as the title, font size, and labels. Since there are no dates yet, we won't label the x-axis.

![sitka high](https://raw.githubusercontent.com/TysonNguyen/PythonCrashCourse_Notes/DownloadingData/Projects/DataVisualization/DownloadingData/July2018_sitka_highs.png "High temperatures July 2018 for Sitka.")

### The datetime Module

Add dates to graph to make it more useful with the first date from the weather data file in second row of the file:

``` markdown
"USW00025333","SITKA AIRPORT, AK US","2018-07-01","0.25",,"62","50"
```

The data will be read in as a string to convert "2018-07-01" to an object representing this date. We can construct an object representing July 1, 2018 using the `strptime()` method from the *datetime* module.

``` python
>>> from datetime import datetime
>>> first_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
>>> print(first_date)
2018-07-01 00:00:00
```

First import the *datetime* class from the module and call the method `strptime()` using the string containing the date as the first argument. The second argument tells Python how the date is formatted. In this example, Python interprets '%Y-' to mean the part of the string before the first dash is a four-digit year; '%m-' represents the month; and '%d' means the last part of the string is the day of the month, from 1 to 31.

The `strptime()` method can take a variety of arguments to determine how to interpret the date.

| Argument  | Meaning                                   |
| ----------| ----------------------------              |
| %A        | Weekday name, such as Monday              |
| %B        | Month name, such as January               |
| %m        | Month as a number (01 to 12)              |
| %d        | Day of the month, as a number (01 to 31)  |
| %Y        | Four-digit year, such as 2019             |
| %y        | Two-digit year, such as 19                |
| %H        | Hour, in 24-hour format (00 to 23)        |
| %I        | Hour, in 12-hour format (01 to 12)        |
| %p        | AM or PM                                  |
| %M        | Minutes (00 to 59)                        |
| %S        | Seconds (00 to 61)                        |

### Plotting Dates

Improve our temperature data plot by extracting dates for the daily highs and passing those highs and dates to `plot()`:

sitka_highs.py

``` python
import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'Projects/DataVisualization/DownloadingData/data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from the file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plots(dates, highs, c='red')

# Format plot.
plt.title("Daily High Temperatures, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
```

1. Create two empty lists to store the dates and high temperatures from the file.

2. Convert the data containing the data information *row([2])* to a *datetime* object and append it to *dates*.

3. Pass the dates and the high temperature values to `plot()`.

4. Call `fig.autofmt_xdate()` draws the date labels diagonally to prevent them from overlapping.

![sitka high with dates](https://raw.githubusercontent.com/TysonNguyen/PythonCrashCourse_Notes/DownloadingData/Projects/DataVisualization/DownloadingData/July2018_sitka_highs_dates.png "High temperatures July 2018 for Sitka with date.")

### Plotting a Longer Timeframe

Now we can generate a graph for the entire year's weather of data with *sitka_weather_2018_simple.csv*.

sitka_highs.py

``` python
--snip--
filename = 'Projects/DataVisualization/DownloadingData/data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    --snip--
# Format plot.
plt.title("Daily High Temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
--snip--
```

1. Modify the filename to use the new data file *sitka_weather_2018_simple.csv*.

2. Update the title of plot to reflect the change in content.

![2018 sitka high with dates](https://raw.githubusercontent.com/TysonNguyen/PythonCrashCourse_Notes/DownloadingData/Projects/DataVisualization/DownloadingData/2018_sitka_highs_dates.png "High temperatures year 2018 for Sitka with date.")

### Plotting a Second Data Series

Make our informative graph more useful by including the low temperatures by extracting them from the data file and then add them to the graph:

sitka_highs_lows.py

``` python
--snip--
filename = 'Projects/DataVisualization/DownloadingData/data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')

# Format plot.
plt.title("Daily Low and High Temperatures - 2018", fontsize=24)
--snip--
```

1. Add the empty list of *lows* to hold low temperatures. 

2. Then extract and store the low temperature for each row position (row[6]).

3. Add a call to `plot()` for the low temperatures and color these values blue.

4. Update the title to represent the new graph.

![2018 sitka high and low temps with dates](https://raw.githubusercontent.com/TysonNguyen/PythonCrashCourse_Notes/DownloadingData/Projects/DataVisualization/DownloadingData/2018_sitka_highs_lows.png "High and low temperatures year 2018 for Sitka with date.")

### Shading an Area in the Chart

With two data series, we can examine the range of temperatures for each day by using shading between the high and low temperatures. Use the `fill_between()` method to take a series of x-values and two series of y-values, and fills the space between the two y-value series:

sitka_highs_lows.py

``` python
--snip--
# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
--snip--
```

1. The alpha argument controls a color's transparency. The values range from 0 to completely transparent, and 1 (default) is completely opaque.

2. Pass the `fill_between()` the list dates for the x-values and then the two y-value series *highs* and *lows*. The facecolor argument determines the color of the shaded region; a low alpha value of 0.1 so the shaded region connects the two data series without distraction.




![2018 sitka high and low temps with shading](https://raw.githubusercontent.com/TysonNguyen/PythonCrashCourse_Notes/DownloadingData/Projects/DataVisualization/DownloadingData/2018_sitka_highs_lows_shade.png "High and low temperatures year 2018 for Sitka with shading.")

The shading helps visualize the range between the two data.

### Error Checking

Some weather stations collect data differently, and some could malfunction and fail to collect some of the data. Missing data can result in exceptions that could cause issues if not handled properly.

The weather data for Death Valley, California using *death_valley_2018_simple.csv* file has different header positions:

death_valley_highs_lows.py

``` python
import csv

filename = 'Projects/DataVisualization/DownloadingData/data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)
```

Here is the output:

``` markdown
0 STATION
1 NAME
2 DATE
3 PRCP
4 TMAX
5 TMIN
6 TOBS
```

The date is in the same position at index 2. The high and low temperatures are at indexes 4 and 5 so we need to change the code to fit the data. Instead of average temperature reading for the day, this station includes TOBS, a reading for specific observation time.

If some data is missing from the file such as temperature reading, we can handle exceptions with `try-except`. It can't turn an empty string to an integer without a value. Running the code gives a ValueError because there is a missing date.

A fix to run error-checking code when the values are being read from the CSV file:

death_valley_highs_lows.py

``` python
import csv
--snip--

filename = 'Projects/DataVisualization/DownloadingData/data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date
            highs.append(high
            lows.append(low)

# Plot the high and low temperatures.
--snip--

# Format plot.
title = "Daily High and Low Temperatures - 2018\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
--snip--
```

1. Each row is examined to extract the date and the high and low temperature.

2. If any data is missing, Python will raise a *ValueError* and handle it by printing an error message that includes the date of the missing data.

3. After printing the error, the loop will continue processing the next row and will run the *else* block to append the data to the lists.

4. Update the title to include the location of the plot and smaller font size because of the longer title.

Only one date had missing data:

``` markdown
Missing data for 2018-02-18 00:00:00
```

Because the error is handled appropriately, the code is able to generate a plot, which skips over the missing data.

![2018 death valley high and low temps with shading](https://raw.githubusercontent.com/TysonNguyen/PythonCrashCourse_Notes/DownloadingData/Projects/DataVisualization/DownloadingData/2018_death_valley_highs_lows.png "High and low temperatures year 2018 for Death Valley.")

Comparing the weather data to Sitka, AK, we notice Death Valley is warmer overall. The range of temperatures each day is greater in the desert.

---

### TRY IT YOURSELF: Download CSV Files

**16-1. Sitka Rainfall**: Sitka is in a temperate rainforest, so it gets a fair amount of rainfall. In the data file *sitka_weather_2018_simple.csv* is a header called *PRCP*, which represents daily rainfall amounts. Make a visualization focusing on the data in this column. You can repeat the exercise for Death Valley if you’re curious how little rainfall occurs in a desert.

**16-2. Sitka–Death Valley Comparison**: The temperature scales on the Sitka and Death Valley graphs reflect the different data ranges. To accurately compare the temperature range in Sitka to that of Death Valley, you need identical scales on the y-axis. Change the settings for the y-axis on one or both of the charts in Figures 16-5 and 16-6. Then make a direct comparison between temperature ranges in Sitka and Death Valley (or any two places you want to compare).

**16-3. San Francisco**: Are temperatures in San Francisco more like temperatures in Sitka or temperatures in Death Valley? Download some data for San Francisco, and generate a high-low temperature plot for San Francisco to make a comparison.

**16-4. Automatic Indexes**: In this section, we hardcoded the indexes corresponding to the TMIN and TMAX columns. Use the header row to determine the indexes for these values, so your program can work for Sitka or Death Valley. Use the station name to automatically generate an appropriate title for your graph as well.

**16-5. Explore**: Generate a few more visualizations that examine any other weather aspect you’re interested in for any locations you’re curious about.

---
