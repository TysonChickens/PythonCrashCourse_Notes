# 15-1 Plot the first five cubic numbers, and then plot first 5000 cubic numbers.

import matplotlib.pyplot as plt

fig, axs = plt.subplots(2)
fig.suptitle("5 to 5000 Cubes")

x_values = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]

axs[0].plot(x_values, cubes)

# Title and label axes.
# plt.title('Cubes', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cubic of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)

# 15-2 Colored cubes

# First 5000 cubic numbers.
x_5000 = list(range(1, 5001))
y_values = [x**3 for x in x_5000]

axs[1].plot(x_5000, y_values)
plt.scatter(x_5000, y_values, c=y_values, cmap=plt.cm.Greens)
plt.axis([0, 5100, 0, 5100**3])

plt.show()


