# PRACTICAL NO 1 - PART 2
# 2. Bar chart
# A bar chart is a graphical representation of data using rectangular bars of equal width,
# where the length or height of each bar is proportional to the value it represents.

import matplotlib.pyplot as plt

x = ["Aman", "suraj", "piyushgupta", "ritesh", "adi"]
y = [78, 68, 63, 58, 78]

plt.bar(x, y, linestyle='-', color='green', label='marks')
plt.title("Simple bar Chart")
plt.xlabel("Names")
plt.ylabel("marks")
plt.legend()
plt.show()
