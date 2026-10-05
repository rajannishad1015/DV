# PRACTICAL NO 3 - PART 8
# 8: 3D Scatter
# A graph that represents each observation as a point in three-dimensional space,
# where the position of the point is determined by its X, Y, and Z values.

import plotly.express as px

df = px.data.tips()
fig = px.scatter_3d(
    df,
    x="total_bill",
    y="tip",
    z="size",
    color="day",
    symbol="sex",
    size="tip",
    opacity=0.8,
    title=" 3D Visualization of Tips Dataset",
    color_discrete_sequence=px.colors.qualitative.Dark24
)
fig.show()
