"""
PRACTICAL NO: 4 (Complete)
Aim: To design and implement interactive data visualization in plotly using dropdown menus, 
buttons and sliders for dynamic data exploration and enhance user interactions.

This script contains both interactive visualizations:
1. Toggle between Line Chart and Bar Chart using update buttons
2. Toggle between Revenue and Profit using a dropdown menu
"""

import plotly.graph_objects as go

# ==========================================
# 1. Line Chart vs Bar Chart (Buttons)
# ==========================================
print("1. Displaying Interactive Line vs Bar Chart with Buttons...")
fig1 = go.Figure()

fig1.add_trace(go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 20, 30, 40],
    mode="lines",
    name="Line"
))

fig1.add_trace(go.Bar(
    x=[1, 2, 3, 4],
    y=[10, 20, 30, 40],
    visible=False,
    name="Bar"
))

fig1.update_layout(
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
fig1.show()

# ==========================================
# 2. Revenue vs Profit (Dropdown Menu)
# ==========================================
print("2. Displaying Interactive Revenue vs Profit Bar Chart with Dropdown...")
fig2 = go.Figure()

fig2.add_trace(go.Bar(
    x=["Jan", "Feb", "Mar"],
    y=[100, 150, 200],
    name="Revenue"
))

fig2.add_trace(go.Bar(
    x=["Jan", "Feb", "Mar"],
    y=[80, 120, 170],
    name="Profit",
    visible=False
))

fig2.update_layout(
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
fig2.show()
