# PRACTICAL NO 3 - PART 6
# 6: Box plot
# A graphical representation that displays the minimum, first quartile (Q1), median (Q2),
# third quartile (Q3), and maximum values of a dataset.

import plotly.express as px

df = px.data.tips()
fig = px.box(
    df,
    x="day",
    y="tip",
    color="day",
    points="all",
    title="       Tip Distribution by Day",
    color_discrete_sequence=px.colors.qualitative.Set2
)
fig.show()
