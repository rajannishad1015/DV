# PRACTICAL NO 2 - PART 5
# 5. Bar plot
# A graphical representation in which bars of equal width are drawn with heights (or lengths) proportional to the values they represent.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")

sns.barplot(x="day", y="total_bill", data=tips)
plt.title("bar Plot of Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()
