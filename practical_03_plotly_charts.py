"""
PRACTICAL NO: 3 (Complete)
Aim: Create Line chart, Bar chart, Scatter plot, Histogram, pie, Box plot, violin plot and 3D Scatter plot using plotly

This script contains all 8 visualizations from Practical 3:
1. Line Chart
2. Bar chart
3. Scatter Plot
4. Histogram
5. Pie Chart
6. Box plot
7. Violin plot
8. 3D Scatter plot
"""

import plotly.express as px

# ==========================================
# 1: Line Chart
# ==========================================
print("1. Displaying Line chart...")
df1 = px.data.iris()
fig1 = px.line(df1, y="sepal_width", title="line chart of sepal length")
fig1.show()

# ==========================================
# 2: Bar chart
# ==========================================
print("2. Displaying Bar chart...")
df2 = px.data.tips()
fig2 = px.bar(
    df2,
    x='day',
    y="total_bill",
    color='sex',
    facet_row='time',
    facet_col='sex',
    title="Average petal length by speacies"
)
fig2.show()

# ==========================================
# 3: Scatter Plot
# ==========================================
print("3. Displaying Scatter plot...")
fig3 = px.scatter(
    df2,
    x='total_bill',
    y="tip",
    color='time',
    symbol='sex',
    size='size',
    facet_row='day',
    facet_col='time'
)
fig3.show()

# ==========================================
# 4: Histogram
# ==========================================
print("4. Displaying Histogram...")
fig4 = px.histogram(
    df2,
    x='total_bill',
    color='sex',
    nbins=50,
    histnorm="percent",
    barmode="overlay"
)
fig4.show()

# ==========================================
# 5: Pie Chart
# ==========================================
print("5. Displaying Pie chart...")
fig5 = px.pie(
    df2,
    values="total_bill",
    names="day",
    color_discrete_sequence=px.colors.sequential.RdBu
)
fig5.show()

# ==========================================
# 6: Box plot
# ==========================================
print("6. Displaying Box plot...")
fig6 = px.box(
    df2,
    x="day",
    y="tip",
    color="day",
    points="all",
    title="       Tip Distribution by Day",
    color_discrete_sequence=px.colors.qualitative.Set2
)
fig6.show()

# ==========================================
# 7: Violin plot
# ==========================================
print("7. Displaying Violin plot...")
fig7 = px.violin(
    df2,
    x="day",
    y="tip",
    color="sex",
    facet_row="time",
    box=True
)
fig7.show()

# ==========================================
# 8: 3D Scatter
# ==========================================
print("8. Displaying 3D Scatter plot...")
fig8 = px.scatter_3d(
    df2,
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
fig8.show()
