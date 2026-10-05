# PRACTICAL NO 3 - PART 4
# 4: Histogram
# A graphical representation of the frequency distribution of continuous data,
# where data is grouped into intervals (bins) and shown using connected bars.

import plotly.express as px

df = px.data.tips()
fig = px.histogram(
    df,
    x='total_bill',
    color='sex',
    nbins=50,
    histnorm="percent",
    barmode="overlay"
)
fig.show()
