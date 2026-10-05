# PRACTICAL NO 3 - PART 1
# 1: Line Chart
# A line chart is a graphical representation of data in which data points are connected by straight lines to show trends, patterns, or changes over time.

import plotly.express as px

df = px.data.iris()
fig = px.line(df, y="sepal_width", title="line chart of sepal length")
fig.show()
