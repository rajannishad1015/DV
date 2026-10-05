# PRACTICAL NO 2 - PART 1
# 1: Line plot
# A line chart is a graphical representation of data in which data points are connected by straight lines to show trends, patterns, or changes over time.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Name": ["piyushgupta", "Adi", "sahil", "santosh"],
    "age": [21, 19, 20, 23]
}
df = pd.DataFrame(data)

sns.lineplot(x=df.index, y='age', data=df)
plt.xlabel("Index")
plt.ylabel("Age")
plt.title("Age line plot")
plt.show()
