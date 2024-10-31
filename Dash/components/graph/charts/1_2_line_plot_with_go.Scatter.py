import plotly.graph_objects as go
import numpy as np


# sample line chart ix and y can be a list
fig = go.Figure(data=go.Scatter(x=x, y=x**2))

# creat empty figure
fig = go.Figure()
# add chart with difrent mode
fig.add_trace(go.Scatter(x=random_x, y=random_y0,
                         mode='lines',
                         name='lines'))
fig.add_trace(go.Scatter(x=random_x, y=random_y1,
                         mode='lines+markers',
                         name='lines+markers'))
fig.add_trace(go.Scatter(x=random_x, y=random_y2,
                         mode='markers', name='markers'))


# put name for traces (will be add as layout) and style line
fig.add_trace(go.Scatter(x=month, y=high_2007, name='High 2007',
                         line=dict(color='firebrick', width=4,
                                   dash='dash'),  # dash options include 'dash', 'dot', and 'dashdot',
                         marker=dict(color="#FFCD05", size=10),
                         ))
