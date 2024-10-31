"""
    Column Definitions:
        Columns are positioned in the grid according to the order the Column Definitions
        You can also use the defaultColDef to apply props to all columns.


        for columns we have :
         
            - defaultColDef: contains properties that all columns will inherit.
                keys for defaultColDef :
                    "resizable", "sortable", "filter", "minWidth", 'editable'
            
            - defaultColGroupDef: contains properties that all column groups will inherit.

            - columnTypes: specific column types containing properties that column definitions can inherit.

            - columnDefs
                keys for columnDefs : 
                    all defaultColDef keys, 'field', 'children', 'cellStyle'


        example:
        # In this example, all the fields are editable except for the "athlete" field
        columnDefs = [
            {'field': 'athlete', 'editable': False},
            {'field': 'sport'},
            {'field': 'age'},
        ]

        defaultColDef = {'editable': True}


    Grouping columns: 
        If you want the columns to be grouped, you can include them as children

    ME :  برای اطلاع دقیق تر دایکومنت مطالعه شود 

    """

import pandas as pd
from dash import Dash, html, dcc
import dash_ag_grid as dag


app = Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

# basic columns definition with column defaults
columnDefs = [
    {"field": "country"},
    {"field": "year"},
    {"field": "athlete"},
    {"field": "age"},
    {"field": "date"},
    {"field": "sport"},
    {"field": "total"},
]

app.layout = html.Div(
    [
        dcc.Markdown(
            "This grid has resizeable columns with sort and filter enabled"),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            columnSize="responsiveSizeToFit",
            defaultColDef={"resizable": True, "sortable": True,
                           "filter": True, "minWidth": 100},
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=False)
