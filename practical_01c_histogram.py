# PRACTICAL NO 1 - PART 3
# 3. Histogram
# It shows the distribution of data by grouping values into bins.
# The hist() function is used to create it with x axis showing bins and y axis showing frequency.

import matplotlib.pyplot as plt

x = [
    7, 8, 9, 10, 10, 12, 12, 12, 13, 14, 14, 15, 16, 16, 17, 18, 18, 19, 20,
    20, 21, 22, 23, 24, 25, 26, 28, 30, 32, 35, 36, 38, 40, 42, 44, 48, 50
]

plt.hist(x, bins=10, linestyle='-', color='red', label='bills ')
plt.title("histogram Chart")
plt.xlabel("totalbills")
plt.ylabel("frequency")
plt.legend()
plt.show()
