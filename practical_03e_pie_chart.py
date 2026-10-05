# PRACTICAL NO 3 - PART 5
# 5: Pie Chart
# It is a circular chart used to show data as proportion or percentages.

import plotly.express as px

df = px.data.tips()
fig = px.pie(
    df,
    values="total_bill",
    names="day",
    color_discrete_sequence=px.colors.sequential.RdBu
)
fig.show()
