"resurses : https://plotly.com/python/bar-charts/"
import plotly.graph_objects as go

# sample bar chart x , y can be list
fig = go.Figure([go.Bar(x=[1, 2, 3], y=[20, 14, 23])])

animals = ['giraffes', 'orangutans', 'monkeys']
# Grouped Bar Chart
fig = go.Figure(data=[
    go.Bar(name='SF Zoo', x=animals, y=[20, 14, 23]),
    go.Bar(name='LA Zoo', x=animals, y=[12, 18, 29])
])
# Change the bar mode
fig.update_layout(barmode='group')  # optian : 'stack'

# Customize aspect
fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)
