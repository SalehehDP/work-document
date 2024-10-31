"""
    according to  following code  and  tile files (generate with QGIS and save in same folder as code)
    we can have map server :)
    we create a app and use it as map server !?
    - the map is going to be limited to min and max and will be bounded (relevant to tiles)

"""
import os.path
from flask import Flask, send_file
import dash_leaflet as dl
from dash import Dash, html

app = Flask(__name__, static_url_path='/static')

# Create app.


@app.route('/requset_map/<zoom>/<y>/<x>', methods=['GET', 'POST'])
def tiles(zoom, y, x):
    default = './tiles/1/1/0.png'  # path to where you have your tile files
    filename = f'./tiles/{zoom}/{x}/{y}.png'
    if os.path.isfile(filename):
        return send_file(filename)
    else:
        return send_file(default)


@app.route('/', methods=['GET', 'POST'])
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(debug=False, host='localhost', port=8080)

    """
    after running the app go to your browser try get "https://0.0.0.0:8080/requset_map/<zoom>/<y>/<x>" => a png
    
    """
