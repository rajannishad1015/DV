# PRACTICAL NO 3 - PART 7
# 7: Violin plot
# A graph that displays the shape of the data distribution, along with the median and quartiles, using a violin-shaped figure.

import plotly.express as px

df = px.data.tips()
fig = px.violin(
    df,
    x="day",
    y="tip",
    color="sex",
    facet_row="time",
    box=True
)
fig.show()
