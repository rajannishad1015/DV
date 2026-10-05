# PRACTICAL NO 1 - PART 1
# 1. Line chart
# A line chart is a graphical representation of data in which data points are connected by straight lines to show trends, patterns, or changes over time.

import matplotlib.pyplot as plt

x = ["jan", "feb", "mar", "apr", "may"]
y = [104, 154, 163, 158, 209]

plt.plot(x, y, marker='o', linestyle='-', color='blue', label='Sales')
plt.title("Simple Line Chart")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.grid(True)
plt.legend()
plt.show()
