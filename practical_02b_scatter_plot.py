# PRACTICAL NO 2 - PART 2
# 2: Scatter Plot
# A scatter plot is a graph that uses dots to represent the relationship between two numerical variables on an X-Y coordinate plane.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "height": [5.5, 6.2, 5.6, 4.9],
    "weight": [56, 67, 45, 40]
}
df = pd.DataFrame(data)

sns.scatterplot(x="height", y='weight', data=df)
plt.xlabel("height")
plt.ylabel("weight")
plt.title("scatter plot")
plt.show()
