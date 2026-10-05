# PRACTICAL NO 3 - PART 2
# 2: Bar chart
# A bar chart is a graphical representation of data using rectangular bars of equal width,
# where the length or height of each bar is proportional to the value it represents.

import plotly.express as px

df = px.data.tips()
fig = px.bar(
    df,
    x='day',
    y="total_bill",
    color='sex',
    facet_row='time',
    facet_col='sex',
    title="Average petal length by speacies"
)
fig.show()
