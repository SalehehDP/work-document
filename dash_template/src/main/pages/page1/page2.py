import dash
import dash_bootstrap_components as dbc


dash.register_page(
    __name__, name='صفحه ۲', external_stylesheets=[dbc.themes.SPACELAB],
    meta_tags=[
        {
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1.0'
        }
    ]
)


layout = dbc.Container([], fluid=True)
