import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, dash_table, callback
import pandas as pd
import numpy as np

from pages.page1.page1 import GraphMaker
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


SIDEBAR_STYLE = {
    "top": 0,
    "right": 0,
    "bottom": 0,
    'fontSize': 30,
    "background-color": "#4C4C4C",
    "color": "#D4D4D4",
    'fontFamily': 'B Badr',
    'height': 965,
}
main_sidebar = html.Div(
    [
        dbc.Nav(
            [
                dbc.NavLink("پایگاه ها", href="/page1",
                            className="page"),
                dbc.NavLink("صحت سنجی", href="/page2",
                            className="page"),
                dbc.NavLink("واگذاری", href="/page3",
                            className="page"),
            ],
            id="main_sidebar",
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE
    # className="main_sidebar"
)

sub_sidebar = html.Div(
    [
        dbc.Nav(
            id="sub_sidebar",
            vertical=True,
            pills=True,
        ),
    ],
    className="sub_sidebar"
)


app.layout = dbc.Container([
    dcc.Location(id="url"),
    dbc.Row(
        [
            dbc.Col([
                dash.html.Img(src=app.get_asset_url('logo.jpg'),
                              style={'height': '90%', 'width': '14%',
                                     'margin-top': "5px", "margin-left": "5px"}
                              ),
            ], style={"background-color": "#000000"}, width=9),
            # dbc.Col([
            #     # dash.html.Div("فراسامانه حکمرانی داده",
            #     #               style={'fontSize': 53, 'textAlign': 'right',
            #     #                      "color": "rgb(255 , 255 , 255)", 'fontFamily': 'B Elham',
            #     #                      'margin-top': "15px", "margin-right": "15px"
            #     #                      }
            #     #               ),
            #         dash.html.Br()
            #         ], style={"background-color": "#000000"}, width=6),
            dbc.Col([
                dash.html.Div("فراسامانه حکمرانی داده",
                              style={'fontSize': 43, 'textAlign': 'right',
                                     "color": "#000000", 'fontFamily': 'B Elham',
                                     'margin-top': "15px", "margin-right": "15px"
                                     }
                              ),
                dash.html.Br()
            ], style={"background-color": "#FFCD05"}, width=3),
        ], className="g-0"
    ),
    dbc.Row([
        dbc.Col(
            [
                html.Div(id="page-content")

            ], width=10
        ),
        # dbc.Col(
        #     [
        #         sub_sidebar
        #     ], width=1
        # ),
        dbc.Col(
            [
                main_sidebar
            ], width=2
        ),
    ],  className="g-0"
    )

], fluid=True

)


@app.callback(
    Output("main_sidebar", "children"),
    Output("page-content", "children"),
    [Input("url", "pathname")])
def render_page_content(pathname):
    nav = []
    path = pathname.split('/')
    print(path)
    if pathname.startswith("/page1"):
        nav = [
            dbc.NavLink("پایگاه ها", href="/page1",
                        className="page"),

            dbc.NavLink("مشترکین", href="/page1/page1",
                        className="page"),
            dbc.NavLink("دارایی فیزیکی", href="/page1/page2",
                        className="page"),
            dbc.NavLink("انرژی", href="/page1/page3",
                        className="page"),
            dbc.NavLink("شبکه و برنامه ریزی", href="/page1/page4",
                        className="page"),
            dbc.NavLink("صحت سنجی", href="/page2",
                        className="page"),
            dbc.NavLink("واگذاری", href="/page3",
                        className="page"),
        ]
        if pathname == "/page1":
            return nav, html.P("")
        if pathname == "/page1/page1":
            graph_maker = GraphMaker()
            map_figure = graph_maker.generatMapFigure()
            pie_chart_faham = graph_maker.generatePieChart_faham()
            pie_chart_type = graph_maker.generatePieChart_type()
            pie_chart_phase = graph_maker.generatePieChart_phase()
            page_content = dbc.Container([
                dbc.Row([
                    dbc.Col([
                        html.Br(),
                        dbc.Row([dcc.Graph(id="pie1", config={
                            'displaylogo': False}, figure=pie_chart_faham),
                        ]),
                        dbc.Row([dcc.Graph(id="pie2", config={
                            'displaylogo': False}, figure=pie_chart_type)]),
                        dbc.Row([dcc.Graph(id="pie3", config={
                            'displaylogo': False}, figure=pie_chart_phase)]),
                    ], width=2),
                    dbc.Col([
                        dash.html.Div("پراکندگی کنتورهای هوشمند",
                                      style={'fontSize': 30, 'textAlign': 'center',
                                             "color": "#000000", 'fontFamily': 'B Badr',
                                             'margin-top': "15px", "margin-right": "15px"
                                             }),
                        dcc.Graph(id="map", config={
                            'displaylogo': False}, figure=map_figure),
                    ], width=10),

                ], className="g-0",
                    style={
                        "background-color": "rgb(255,255,255)"  # "#ECEBEB",
                }),
            ], fluid=True
            )
            return nav, page_content
        else:
            return nav, html.P("")

    if pathname == "/page2":
        df = pd.DataFrame({
            'شرح تناقض': ["یکسان نیست CT , PT ضریب"] + ["" for i in range(1, 20)],
            'شماره رمز رایانه': [i * 100 for i in range(1, 21)],
            'شماره کنتور': [i * 1111 for i in range(1, 21)]
        })
        page_content = dbc.Container([
            html.Br(),
            dbc.Row([
                dbc.Col([html.Br()], width=3),
                dbc.Col([
                    dcc.Dropdown(['پایگاه داده ۱', 'پایگاه داده ۲', 'پایگاه داده ۳'],
                                 'پایگاه داده ۱', id='drop1',
                                 style={"margin-left": "15px", "width": "220px",
                                        'textAlign': 'right', 'fontSize': 25,
                                        "color": "#000000", 'fontFamily': 'B Badr', },
                                 ),
                ]),
                dbc.Col([
                    dcc.Dropdown(['پایگاه داده ۱', 'پایگاه داده ۲', 'پایگاه داده ۳'],
                                 'پایگاه داده ۲', id='drop1',
                                 style={"margin-left": "15px", "width": "220px", "align": "center",
                                        'textAlign': 'right', 'fontSize': 25,
                                        "color": "#000000", 'fontFamily': 'B Badr', },
                                 ),
                ])
            ]),
            html.Br(),
            dash_table.DataTable(df.to_dict('records'), [
                                 {"name": i, "id": i} for i in df.columns],
                                 page_size=10,
                                 # style_table={'minWidth': '100%'},
                                 style_cell_conditional=[
                {'if': {'column_id': 'شرح تناقض'},
                 'width': '50%'},
            ],
                style_header={
                'backgroundColor': "#d9d9d9",
                'fontWeight': 'bold',
                'fontFamily': "B Badr",
                'fontSize': 30
            },
                style_data={
                'backgroundColor': "#f2f2f2",
                'color': 'black',
                'fontFamily': "B Badr",
                'fontSize': 28
            },
                # style_table={
                #    'height': '300px', 'overflowY': 'auto'},
                id='tbl'),
        ],
            # fluid=True
        )
        return main_sidebar, page_content
    if pathname == "/page3":
        page_content = dbc.Container(
            [
                # html.Col([
                dbc.Row([
                    dbc.Col([html.Br()], width=4),
                    dbc.Col([
                        dash.html.Div("اعطای مجوز  ",
                                      style={'fontSize': 33, 'textAlign': 'center',
                                             "color": "#000000", 'fontFamily': 'B Badr',
                                             'margin-top': "15px", "margin-right": "15px"
                                             }
                                      ),
                        dbc.Row([

                            dcc.Input(id="auth", type="text",
                                      placeholder="مشخصات کاربر",
                                      style={
                                          'textAlign': 'right', 'fontSize': 25,
                                          "color": "#000000", 'fontFamily': 'B Badr',
                                      }

                                      ),

                        ],
                        ),

                        dbc.Row([
                            dcc.Input(
                                id="from", type="text",
                                placeholder="از تاریخ",
                                style={
                                    'textAlign': 'right', 'fontSize': 25,
                                    "color": "#000000", 'fontFamily': 'B Badr',
                                }
                                # min=10, max=100, step=3,
                            ),
                        ],
                        ),
                        dbc.Row([

                            dcc.Input(
                                id="to", type="text",
                                debounce=True, placeholder="تا تاریخ",
                                style={
                                    'textAlign': 'right', 'fontSize': 25,
                                    "color": "#000000", 'fontFamily': 'B Badr',
                                }
                            ),
                        ],
                        ),

                        dbc.Row([
                            dcc.Dropdown(['وب سرویس ۱', 'وب سرویس ۲', 'وب سرویس ۳'],
                                         'وب سرویس ۱', id='web',
                                         style={"margin-left": "15px",
                                                'textAlign': 'right', 'fontSize': 25,
                                                "color": "#000000", 'fontFamily': 'B Badr', },
                                         ),
                            html.Br()],
                        ),
                        # ],
                        #    width=3),
                        dbc.Row([], id="table")
                        # html.Div(id="number-out"),
                    ], width=4),

                ])
            ], fluid=True
        )
        return main_sidebar, page_content

    return main_sidebar, html.Div(
        [
            #html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            #html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


# @ callback(Output('tbl_out', 'children'), Input('tbl', 'active_cell'))
# def update_graphs(active_cell):
#     return str(active_cell) if active_cell else "Click the table"

@ callback(Output('table', 'children'),
           Input('web', 'value'),
           Input('auth', 'value'),
           Input('from', 'value'),
           Input('to', 'value'),
           )
def update_graphs(web, auth, from_date, to_date):
    if to_date is not None and from_date is not None and auth is not None:
        df = pd.DataFrame({
            "وب سرویس واگذاری شده": [web for i in range(1, 21)],
            'تا تاریخ': [to_date for i in range(1, 21)],
            'از تاریخ': [from_date for i in range(1, 21)],
            'مشحصات کاربر': [auth for i in range(1, 21)]
        })
    else:
        df = pd.DataFrame({
            "وب سرویس واگذاری شده": [],
            'تا تاریخ': [],
            'از تاریخ': [],
            'مشحصات کاربر': []
        })
    table = dash_table.DataTable(df.to_dict('records'), [
        {"name": i, "id": i} for i in df.columns],
        page_size=10,
        # style_table={'minWidth': '100%'},
        style_cell_conditional=[
        {'if': {'column_id': 'شرح تناقض'},
         'width': '50%'},
    ],
        style_header={
        'backgroundColor': "#d9d9d9",
        'fontWeight': 'bold',
        'fontFamily': "B Badr",
        'fontSize': 30
    },
        style_data={
        'backgroundColor': "#f2f2f2",
        'color': 'black',
        'fontFamily': "B Badr",
        'fontSize': 28
    },
        # style_table={
        #    'height': '300px', 'overflowY': 'auto'},
        id='tbl')
    return table


if __name__ == "__main__":
    app.run(
        host="0.0.0.0", port=8200, debug=False)
