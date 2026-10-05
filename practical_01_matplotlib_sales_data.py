"""
PRACTICAL NO: 1 (Complete)
Aim: Visualization basic sales data using matplotlib
Objective: Data visualization using matplotlib and python by creating and customize different 
charts such as bar line pie scatter histogram all sales data set to add title axis labels color markers 
for effective presentation

This script contains all 5 visualizations from Practical 1:
1. Line chart
2. Bar chart
3. Histogram
4. Scatter chart
5. Pie chart
"""

import matplotlib.pyplot as plt

# ==========================================
# 1. Line chart
# ==========================================
print("Generating 1. Line chart...")
x = ["jan", "feb", "mar", "apr", "may"]
y = [104, 154, 163, 158, 209]
plt.figure()
plt.plot(x, y, marker='o', linestyle='-', color='blue', label='Sales')
plt.title("Simple Line Chart")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.grid(True)
plt.legend()
plt.show()

# ==========================================
# 2. Bar chart
# ==========================================
print("Generating 2. Bar chart...")
x = ["Aman", "suraj", "piyushgupta", "ritesh", "adi"]
y = [78, 68, 63, 58, 78]
plt.figure()
plt.bar(x, y, linestyle='-', color='green', label='marks')
plt.title("Simple bar Chart")
plt.xlabel("Names")
plt.ylabel("marks")
plt.legend()
plt.show()

# ==========================================
# 3. Histogram
# ==========================================
print("Generating 3. Histogram...")
x = [
    7, 8, 9, 10, 10, 12, 12, 12, 13, 14, 14, 15, 16, 16, 17, 18, 18, 19, 20,
    20, 21, 22, 23, 24, 25, 26, 28, 30, 32, 35, 36, 38, 40, 42, 44, 48, 50
]
plt.figure()
plt.hist(x, bins=10, linestyle='-', color='red', label='bills ')
plt.title("histogram Chart")
plt.xlabel("totalbills")
plt.ylabel("frequency")
plt.legend()
plt.show()

# ==========================================
# 4. Scatter chart
# ==========================================
print("Generating 4. Scatter chart...")
x = [10, 15, 20, 25, 30]
y = [12, 18, 25, 28, 35]
plt.figure()
plt.scatter(x, y, linestyle='--', color='yellow', label='random')
plt.title("scatter Chart")
plt.xlabel("x data")
plt.ylabel("y data")
plt.grid(False)
plt.legend()
plt.show()

# ==========================================
# 5. Pie chart
# ==========================================
print("Generating 5. Pie chart...")
labels = ["AUDI", "BMW", "FORD", "TESLA", "JAGUAR"]
sizes = [23, 10, 35, 15, 12]
plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("pie chart ")
plt.xlabel("sales")
plt.ylabel("car")
plt.legend()
plt.show()
