
"""
    resource : https://dash.plotly.com/dash-daq/numericinput

    """
import dash_daq as daq

# smaple numberic input
daq.NumericInput(
    id='my-numeric-input-1',
    value=0,  # init value
    label='Label',  # add lable
    labelPosition='bottom',
    size=120,  # width ?
    min=1,  # min value
    max=30,  # max value
),
