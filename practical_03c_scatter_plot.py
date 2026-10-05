# PRACTICAL NO 3 - PART 3
# 3: Scatter Plot
# A graphical method used to show the relationship between two variables. Each point on the graph represents one observation with an x-value and a y-value.

import plotly.express as px

df = px.data.tips()
fig = px.scatter(
    df,
    x='total_bill',
    y="tip",
    color='time',
    symbol='sex',
    size='size',
    facet_row='day',
    facet_col='time'
)
fig.show()
