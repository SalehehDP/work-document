"""
    resurses : https://plotly.com/python/line-charts/

    """

import plotly.express as px

# sample linechart with title
fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')

# multi linechart with diffrent color will be added
fig = px.line(df, x="year", y="lifeExp", color='country')

# put text for each marker in linechart
fig = px.line(df, x="lifeExp", y="gdpPercap", color="country", text="year")
# adjust text position
fig.update_traces(textposition="bottom right")

# add ' markers = True ' if you need marker too
fig = px.line(df, x='year', y='lifeExp', color='country', markers=True)

# multi linechart with diffrent symbol will be added
fig = px.line(df, x='year', y='lifeExp', color='country', symbol="country")
