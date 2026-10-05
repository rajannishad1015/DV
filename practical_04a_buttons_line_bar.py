# PRACTICAL NO 4 - PART 1
# AIM: Interactive visualization with buttons to toggle between Line Chart and Bar Chart

import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 20, 30, 40],
    mode="lines",
    name="Line"
))

fig.add_trace(go.Bar(
    x=[1, 2, 3, 4],
    y=[10, 20, 30, 40],
    visible=False,
    name="Bar"
))

fig.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            buttons=[
                dict(
                    label="Line Chart",
                    method="update",
                    args=[{"visible": [True, False]}]
                ),
                dict(
                    label="Bar Chart",
                    method="update",
                    args=[{"visible": [False, True]}]
                )
            ]
        )
    ]
)

fig.show()
