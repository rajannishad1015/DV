"""
PRACTICAL NO: 2 (Complete)
Aim: Create lineplot, scatter plot, box plot, violin plot, bar plot using seaborn

This script contains all 5 visualizations from Practical 2:
1. Line plot
2. Scatter Plot
3. Box plot
4. Violin plot
5. Bar plot
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. Line plot
# ==========================================
print("Generating 1. Line plot...")
data = {
    "Name": ["piyushgupta", "Adi", "sahil", "santosh"],
    "age": [21, 19, 20, 23]
}
df1 = pd.DataFrame(data)
plt.figure()
sns.lineplot(x=df1.index, y='age', data=df1)
plt.xlabel("Index")
plt.ylabel("Age")
plt.title("Age line plot")
plt.show()

# ==========================================
# 2. Scatter Plot
# ==========================================
print("Generating 2. Scatter plot...")
data = {
    "height": [5.5, 6.2, 5.6, 4.9],
    "weight": [56, 67, 45, 40]
}
df2 = pd.DataFrame(data)
plt.figure()
sns.scatterplot(x="height", y='weight', data=df2)
plt.xlabel("height")
plt.ylabel("weight")
plt.title("scatter plot")
plt.show()

# ==========================================
# 3. Box plot
# ==========================================
print("Generating 3. Box plot...")
data = {
    "Name": ["piyushgupta", "Adi", "sahil", "santosh"],
    "marks": [56, 67, 45, 40]
}
df3 = pd.DataFrame(data)
plt.figure()
sns.boxplot(y="marks", data=df3, color="blue")
plt.xlabel("name of student")
plt.ylabel("marks")
plt.title("box plot")
plt.show()

# ==========================================
# 4. Violin plot
# ==========================================
print("Generating 4. Violin plot...")
tips = sns.load_dataset("tips")
plt.figure()
sns.violinplot(x="day", y="total_bill", data=tips)
plt.title("violin Plot of Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()

# ==========================================
# 5. Bar plot
# ==========================================
print("Generating 5. Bar plot...")
plt.figure()
sns.barplot(x="day", y="total_bill", data=tips)
plt.title("bar Plot of Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()
