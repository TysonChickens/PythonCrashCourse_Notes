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
ax.set_ylabel("Square of Value", fontsize=14)

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
import matplotlib.pyplot as plt

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

## Random Walks

We will use Python to generate data for a random walk, and then use Matplotlib to create a visually appealing representation of data. A ***random walk*** is a path that has no clear direction but is determined by a series of random decisions.

Random walks have practical applications in nature, physics, biology, chemistry, and economics. For example, a pollen grain floating on a drop of water moves across the surface of the water because it is constantly pushed around by water molecules. Molecular motion in a water drop is random, so the path a pollen grain traces on the surface is a random walk, which can model many real-world situations.

### Creating the RandomWalk() Class

To create a random walk, we will create a *RandomWalk* class, which will make random decisions about which direction the walk should be. The class needs three attributes:

1. A variable to store the number of points in the walk.

2. A list to store the x-coordinates.

3. A list to store the y-coordinates.

We need two methods for the *RandomWalk* class:

1. The `__init__()` method.

2. `fill_walk()` to calculate the points in the walk.

random_walk.py

``` python
from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]
```

To make random decisions, we store possible moves in a list and use `choice()` function, from the *random* module, to decide which move to make each time a step is taken. We set the default number of points in a walk to 5000 points, which is large enough to generate interesting patterns. Then we make two lists to hold x- and y-values, and start each walk at the point (0, 0).

### Choosing Directions

Use the *fill_walk()* method to fill our walk with points and determine the direction of each step. Add this method to *random_walk.py*:

``` python
def fill_walk(self):
    """Calculate all the points in the walk."""

    # Keep taking steps until the walk reaches the desired length."""
    while len(self.x_values) < self.num_points:

        # Decide which direction to go and how far to go in that direction.
        x_direction = choice([1, -1])
        x_distance = choice([0, 1, 2, 3, 4])
        x_step = x_direction * x_distance

        y_direction = choice([1, -1])
        y_distance = choice([0, 1, 2, 3, 4])
        y_step = y_direction * y_distance

        # Reject moves that go nowhere.
        if x_step == 0 and y_step == 0:
            continue

        # Calculate new position.
        x = self.x_values[-1] + x_step
        y = self.y_values[-1] + y_step

        self.x_values.append(x)
        self.y_values.append(y)
```

1. A loop that runs until the walk is filled with the correct number of points. We use *choice([1, -1])* to choose a value for *x_direction*, which returns either 1 for right movement or -1 for left.

2. *choice([0, 1, 2, 3, 4])* tells Python how far to move in that direction (x_distance) by randomly selecting an integer between 0 and 4. The inclusion of 0 allows to take steps along the y-axis as well as steps that have movement along both axes.

3. We determine the length of each step in the x and y directions by multiplying the direction of movement by the distance chosen. A positive result for *x_step* means move right, a negative result means move left, and 0 means move vertically. A positive result for *y_step* means move up, negative means move down, and 0 means move horizontally. If the value of both *x_step* and *y_step* are 0, the walk does not go anywhere, so we can continue the loop to ignore this move.

4. To get the next x-value for the walk, we add the value in *x_step* to the last value stored in *x_values* and do the same for the y-values. When we have these values, we append them to *x_values* and *y_values*.

### Plotting the Random Walk

Code to plot all the points in the walk:

rw_visual.py

``` python
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk()
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
```

1. Begin by importing `pyplot` and *RandomWalk*.  Create a random walk and store it in *rw* with a call to *fill_walk()*.

2. Feed the walk's x- and y-values to `scatter()` and choose an appropriate dot size.

![alt text](https://raw.githubusercontent.com/TysonNguyen/PythonCrashCourse_Notes/DataVisualization/Projects/DataVisualization/FirstRandomWalk.png "Random walk.")

### Generating Multiple Random Walks

Every random walk is different and can keep being generated without having to run the program multiple times with a while loop:

rw_visual.py

``` python
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
```

When the Matplotlib viewer is closed, a prompt will show up and ask if we want to generate another walk.

### Styling the Walk

Customize the plots to emphasize the important characteristics of each walk an deemphasize distracting elements. We have to identify the characteristics we want to emphasize, such as where the walk began, where it ended, and the path taken. Next, identify what to deemphasize, such as tick marks and labels. The result should be a simple visual representation that clearly communicates the path taken in each random walk.

#### Coloring the Points

We use a colormap to show the order of the points in the walk, and then remove the black outline from each dot so the color of the dots will be clearer. To color the points according to their position in the walk, we pass the *c* argument a list containing the position of each point from numbers 0 to 4999:

rw_visual.py

``` python
--snip--
while True:
    # Make a random walk.
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
```

We use `range()` to generate a list of numbers equal to the number of points in the walk. Then we store them in the list of *point_numbers* to the *c* argument, use *Blues* colormap, and then pass `edgecolors='none'` to get rid of the black outline around each point with a light to dark blue gradient.

![alt text](https://raw.githubusercontent.com/TysonNguyen/PythonCrashCourse_Notes/DataVisualization/Projects/DataVisualization/ColorRandomWalk.png "Random walk with style and colors.")

#### Plotting the Starting and Ending Points

In addition to coloring the points, we can see where each walk begins and ends by plotting the first and last points individually.

rw_visual.py

``` python
--snip--
while True:
    --snip--
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    plt.show()
    --snip--
```

To show the starting point, we plot point (0, 0) in green in larger size (s=100) than the rest of the points. To mark the end point, we plot the last x- and y-value in the walk in red with a size of 100.

#### Cleaning Up the Axes

To remove the axes in this plot for a clear path of each walk:

``` python
--snip--
while True:
    --snip--
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    --snip--
```

Both x- and y-axis are modified to set the visibility to False to remove them.

#### Adding Plot Points

We increase the value of *num_points* when we make a *RandomWalk* instance to add more points and data to work with.

rw_visual.py

``` python
--snip--
while True:
    # Make a random walk.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots()

    # Color / Style the points in the walk.
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    --snip--
```

This example creates a random walk with 50,000 points (to mirror real-world data) and plots each point at size `s=1`.

![alt text](https://raw.githubusercontent.com/TysonNguyen/PythonCrashCourse_Notes/DataVisualization/Projects/DataVisualization/50000RandomWalk.png "Random walk of 50,000 points start/end and colors.")

#### Altering the Size to Fill the Screen

A visualization is more effective at communicating patterns in data if it fits nicely on the screen. We can adjust the size of Matplotlib's output window:

rw_visual.py

``` python
--snip--
while True:
    # Make a random walk.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    --snip--
```

When creating the plot, the `figsize` argument allows to set the size of the figure. The parameter takes a tuple, which tells Matplotlib the dimensions of the plotting window in inches.

Matplotlib assumes that a screen resolution is 100 pixels per inch. If we know the system's resolution, pass `plt.subplots()` the resolution using the `dpi` parameter to set a plot size that makes effective use of the space available on the screen:

``` python
fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
```

---

### TRY IT YOURSELF: Random Walks

**15-3. Molecular Motion**: Modify rw_visual.py by replacing `plt.scatter()` with `plt.plot()`. To simulate the path of a pollen grain on the surface of a drop of water, pass in the *rw.x_values* and *rw.y_values*, and include a linewidth argument. Use 5000 instead of 50,000 points.

**15-4. Modified Random Walks**: In the RandomWalk class, *x_step* and *y_step* are generated from the same set of conditions. The direction is chosen randomly from the list [1, -1] and the distance from the list [0, 1, 2, 3, 4]. Modify the values in these lists to see what happens to the overall shape of your walks. Try a longer list of choices for the distance, such as 0 through 8, or remove the −1 from the x or y direction list.

**15-5. Refactoring**: The *fill_walk()* method is lengthy. Create a new method
called *get_step()* to determine the direction and distance for each step, and
then calculate the step. You should end up with two calls to *get_step()* in
*fill_walk()*:

* x_step = self.get_step()

* y_step = self.get_step()

This refactoring should reduce the size of *fill_walk()* and make the method easier to read and understand.

---
