# PRACTICAL NO 4 - PART 2
# AIM: Interactive visualization with dropdown menu to toggle between Revenue and Profit

import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Bar(
    x=["Jan", "Feb", "Mar"],
    y=[100, 150, 200],
    name="Revenue"
))

fig.add_trace(go.Bar(
    x=["Jan", "Feb", "Mar"],
    y=[80, 120, 170],
    name="Profit",
    visible=False
))

fig.update_layout(
    updatemenus=[
        dict(
            buttons=[
                dict(
                    label="Revenue",
                    method="update",
                    args=[{"visible": [True, False]},
                          {"title": "Revenue"}]
                ),
                dict(
                    label="Profit",
                    method="update",
                    args=[{"visible": [False, True]},
                          {"title": "Profit"}]
                )
            ],
            direction="down",
            showactive=True
        )
    ]
)

fig.show()
