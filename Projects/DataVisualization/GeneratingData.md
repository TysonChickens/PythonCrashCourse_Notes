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

![alt text](https://raw.githubusercontent.com/TysonNguyen/PythonCrashCourse_Notes/DataVisualization/Projects/DataVisualization/original.png "Basic plot line graph")


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

![alt text](https://raw.githubusercontent.com/TysonNguyen/PythonCrashCourse_Notes/DataVisualization/Projects/DataVisualization/originalV2.png "Updated plot with title and labeled axes.")

1. The *linewidth* parameter controls the thickness of the line that `plot()` generates.

2. `set_title()` method sets a title for the chart and fontsize control the size of the text in various elements on the chart.

3. `set_xlabel()` and `set_ylabel()` methods allow to set a title for each of the axes.

4. `tick_params()` method styles the tick marks on both axes of the graph with font size of 14.

### Correcting the Plot

The data is not plotted correctly due to the square of 4.0 is shown as 25.

When `plot()` is given a sequence of numbers, it assumes the first data point corresponds to an x-coordinate value of 0, but our first value point correctly responds to an x-value of 1. We can override the default behavior by giving `plot()` the input and output values used to calculate the squares:

mpl_squares.py

``` python
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
--snip--
```

Now `plot()` will graph the data correctly because provided the input and output values, so it doesn't have to assume how the output numbers were generated.

### Plotting and Styling Individual Points with scatter()

Sometimes, it is useful to plot and style individual points based on certain characteristics for clear graphs.

To plot a single point, use the `scatter()` method. Pass the single (x, y) values of the point of interest to `scatter()` to plot those values:

scatter_squares.py

``` python
import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2, 4)

plt.show()
```

We can make the output more interesting with a title, labeled axes, and a readable font size:

``` python
import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsizes=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
```

The *s* argument in ax.scatter sets the size of the dots used to draw the graph. We should now see a single point in the middle of the chart.

### Plotting a Series of Points with Scatter()

To plot a series of points, we can pass `scatter()` separate lists of x- and y- values:

scatter_squares.py

``` python
import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

# Set chart title and label axes.
--snip--
```

The *x_values* list contains the numbers to be squared, and *y_values* contains the square of each number. When these lists are passed to `scatter()`, Matplotlib reads one value from each list as it plots each point.

### Calculating Data Automatically

Writing list by hand can be inefficient, and Python can loop through a list to do the calculations for us.

scatter_squares.py with 1000 points:

``` python
import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

# Set chart title and label axes.
--snip--

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

plt.show()
```

1. Start with a range of x-values containing the numbers 1 through 1000. A list comprehension generates the y-values by looping through the x-values (for x in x_values), squaring each number (x**2) and storing the results in y_values.

2. Since this is a large data set, we use a smaller point size for `scatter()` argument.

3. We use the `axis()` method to specify the range of each axis. The `axis()` method requires four values: the minimum and maximum values for the x-axis and y-axis. Here, we run the x-axis from 0 to 1100 and the y-axis from 0 to 1,100,000.

### Defining Custom Colors

To change the color of hte points, pass *c* to `scatter()` with the name of a color to use in quotation marks, as show here:

``` python
ax.scatter(x_values, y_values, c='red', s=10)
```

We can also define a custom color using the RGB color model with a tuple using three decimal values, using values between 0 and 1. For example, the following lines creates a plot with light-green dots:

``` python
ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)
```

Values closer to 0 produce dark colors, and values closer to 1 produce lighter colors.

scatter_squares.py colormap

### Using a Colormap

A ***colormap*** is a series of colors in a gradient that moves from a starting to an ending color. Colormaps in a visualization emphasize a pattern in the data. For example, might make low values a light color and high values a darker color.

The *pyplot* module includes a set of built-in colormaps. To use colormaps, specify how pyplot should assign a color to each point in the data set. 

scatter_squares.py colormaps with y-values:

```python
import matploblib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes.
--snip--
```

We pass the list of y-values to c, and then tell pyplot which colormap to use using the *cmap* argument. This code colors the points with lower y-values light blue and colors the points with higher y-values dark blue.

### Saving Plots Automatically

If we want to save the plot to a file, we can replace the call to `plt.show()` wih a call to `plt.savefig()`:

``` python
plt.savefig('squares_plot.png', bbox_inches='tight')
```

The first argument is a filename for the plot image. The second argument trims extra whitespace from the plot. If we want extra whitespace around the plot, omit the argument.

---

### TRY IT YOURSELF: Plotting Graphs

**15-1. Cubes**: A number raised to the third power is a cube. Plot the first five cubic numbers, and then plot the first 5000 cubic numbers.

**15-2. Colored Cubes**: Apply a colormap to your cubes plot.

---