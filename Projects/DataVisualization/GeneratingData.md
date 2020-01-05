# Data Visualization

Data visualization involves exploring data through visual representations. It is closely associate with data analysis, which uses code to explore the patterns and connections in a data set. A data set can be made up of a small list of numbers that fits in one line of code or many gigabytes of data.

We can see patterns and significance in data-intensive work in genetics, climate research, political and economic analysis, and much more. Python has many tools available of visualization and analysis almost everyone can use.

## Installing Matplotlib

Enter command to terminal prompt to install Matplotlib package via the pip module in Python:

``` markdown
python -m pip install --user matplotlib
```

## Plotting a Simple Line Graph

Matplotlib can plot a simple line graph, and then customize it to create a more information data visualization. Here, we use the square number sequence 1, 4, 9, 16, 25 as the data for the graph:

mpl_squares.py

``` python
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares)

plt.show()
```

![Unedited plot](https://raw.githubusercontent.com/TysonNguyen/PythonCrashCourse_Notes/DataVisualization/Projects/DataVisualization/original.png)


1. Import the `pyplot` module using the alias *plt*. The pyplot module contains a number of functions that generate charts and plots.

2. Create a list called *squares* to hold the data to plot, and then call the `subplots()` function to generate one or more plots in the same figure. The variable *ax* represents a single plot in the figure and is the variable used most of the time.

3. Use the `plot()` method, which will try to plot the data it is given in a meaningful way. The function `plt.show()` opens Matplotlib's viewer and displays the plot.

### Changing the Label Type and Line Thickness

Use the available customizations to improve the plot's readability because the label type is too small and the line is a bit thin:

``` python
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()
```

![Updated plot with title and labeled axes.](https://raw.githubusercontent.com/TysonNguyen/PythonCrashCourse_Notes/DataVisualization/Projects/DataVisualization/originalV2.png)

1. The *linewidth* parameter controls the thickness of the line that `plot()` generates.

2. `set_title()` method sets a title for the chart and fontsize control the size of the text in various elements on the chart.

3. `set_xlabel()` and `set_ylabel()` methods allow to set a title for each of the axes.

4. `tick_params()` method styles the tick marks on both axes of the graph with font size of 14.
