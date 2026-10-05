# PRACTICAL NO 2 - PART 4
# 4. Violin plot
# A graph that displays the shape of the data distribution, along with the median and quartiles, using a violin-shaped figure.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")

sns.violinplot(x="day", y="total_bill", data=tips)
plt.title("violin Plot of Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()
