# PRACTICAL NO 1 - PART 4
# 4. Scatter chart
# It is used to observe relationship between variables. The scatter() method in matplotlib library is used to draw.

import matplotlib.pyplot as plt

x = [10, 15, 20, 25, 30]
y = [12, 18, 25, 28, 35]

plt.scatter(x, y, linestyle='--', color='yellow', label='random')
plt.title("scatter Chart")
plt.xlabel("x data")
plt.ylabel("y data")
plt.grid(False)
plt.legend()
plt.show()
