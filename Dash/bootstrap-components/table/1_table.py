"""
    resours : https://dash-bootstrap-components.opensource.faculty.ai/docs/components/table/
    """


import dash_bootstrap_components as dbc
from dash import html

table_header = [
    html.Thead(html.Tr([html.Th("First Name"), html.Th("Last Name")]))
]

row1 = html.Tr([html.Td("Arthur"), html.Td("Dent")])
row2 = html.Tr([html.Td("Ford"), html.Td("Prefect")])
row3 = html.Tr([html.Td("Zaphod"), html.Td("Beeblebrox")])
row4 = html.Tr([html.Td("Trillian"), html.Td("Astra")])

table_body = [html.Tbody([row1, row2, row3, row4])]

table = dbc.Table(table_header + table_body, bordered=True)


# create table from dataframe
table = dbc.Table.from_dataframe(
    df, striped=True, bordered=True, hover=True, index=True
)

"""
    bordered (boolean; optional): Apply the table-bordered class which adds borders on all sides of the table and cells.

    borderless (boolean; optional): Apply the table-borderless class which removes all borders from the table and cells.

    striped (boolean; optional): Apply the table-striped class which applies 'zebra striping' to rows in the table body.
    
    hover (boolean; optional): Apply the table-hover class which enables a hover state on table rows within the table body.
    
    """
