# PRACTICAL NO 2 - PART 3
# 3. Box plot
# A box plot is a statistical graph that represents a dataset using the minimum, first quartile, median,
# third quartile, and maximum values to show the distribution and spread of the data.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Name": ["piyushgupta", "Adi", "sahil", "santosh"],
    "marks": [56, 67, 45, 40]
}
df = pd.DataFrame(data)

sns.boxplot(y="marks", data=df, color="blue")
plt.xlabel("name of student")
plt.ylabel("marks")
plt.title("box plot")
plt.show()
