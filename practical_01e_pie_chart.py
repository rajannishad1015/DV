# PRACTICAL NO 1 - PART 5
# 5. Pie chart
# It is a circular chart used to show data as proportion or percentages.

import matplotlib.pyplot as plt

labels = ["AUDI", "BMW", "FORD", "TESLA", "JAGUAR"]
sizes = [23, 10, 35, 15, 12]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("pie chart ")
plt.xlabel("sales")
plt.ylabel("car")
plt.legend()
plt.show()
