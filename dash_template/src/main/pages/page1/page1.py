import plotly.express as px
import plotly.graph_objects as go
import pathlib
from typing import Dict, Any, List
import json


class GraphMaker:

    def read(self) -> Dict[str, Any]:
        # need two func from meterData and mapConfig
        path = pathlib.Path(
            "resources/main", "meter.json")
        if not path.exists():
            raise RuntimeError(
                "Could not find the start mode config file.")

        with open(path, 'r') as j:
            contents = json.loads(j.read())

        return contents

    def generatMapFigure(self) -> go.Figure:
        meterData = self.read()["meterData"]
        mapFigure = px.scatter_mapbox(
            meterData, lat="lat", lon="lon",
            custom_data=['id', 'ramz_rayane',
                         "دسترسی پذیری", 'phase', 'feeder', 'وضعیت'],
        )
        mapFigure.update_traces(marker=dict(
            size=8, color="#82CCDE"  # "rgb(21, 152, 62)"
        ))
        mapFigure.update_layout(
            mapbox_style='open-street-map',
            margin={"r": 40, "t": 15,
                    "l": 40, "b": 5},
            height=900,
            paper_bgcolor="rgb(255,255,255)"  # "#ECEBEB",
        )
        # self.__addHoverOfMeterInformationOnMapFigure()
        return mapFigure

    def generatePieChart_faham(self) -> go.Figure:
        labels = ['فهام ۱', 'فهام ۲']
        pie_chart_faham = go.Figure(
            data=[go.Pie(labels=labels, values=[1000, 2500],
                         title="فهام ۱ و فهام ۲",
                         title_font_size=30,
                         hole=.3,
                         # pull=[0, 0, 0.2, 0.2],
                         marker_colors=["#6D4DCC", "#AC4DCC"],

                         )]
        )

        pie_chart_faham.update(layout_showlegend=False)
        pie_chart_faham.update_layout(
            margin=dict(t=20, l=0, r=0, b=0),
            paper_bgcolor="rgb(255,255,255)",  # "#ECEBEB",
            font_family="B Badr",
            font_size=20,
            height=300,


        )
        pie_chart_faham.update_layout(
            hoverlabel=dict(
                # bgcolor="white",
                font_family="B Badr",
                font_size=20,
            ),
            hoverlabel_align='right')

        return pie_chart_faham

    def generatePieChart_type(self) -> go.Figure:
        labels = ["ثانویه", "اولیه"]
        pie_chart_type = go.Figure(
            data=[go.Pie(labels=labels, values=[6000, 500],
                         title="اولیه و ثانویه",
                         title_font_size=30,
                         hole=.3,
                         # pull=[0, 0, 0.2, 0.2],
                         marker_colors=["#4DACCC", "#4D6DCC"],
                         # height=300,

                         )]
        )

        pie_chart_type.update(layout_showlegend=False)
        pie_chart_type.update_layout(
            margin=dict(t=20, l=0, r=0, b=0),
            paper_bgcolor="rgb(255,255,255)",  # "#ECEBEB",
            font_family="B Badr",
            font_size=20,
            height=300,

            # title={
            #     'text': "اولیه و ثانویه",
            #     # 'y': 0.9,
            #     # 'x': 0.5,
            #     'xanchor': 'center',
            #     # 'yanchor': 'top',
            #     'font_family': "B Badr",
            #     'font_size': 20,

            # }
        )

        pie_chart_type.update_layout(
            hoverlabel=dict(
                # bgcolor="white",
                font_family="B Badr",
                font_size=20,
            ),
            hoverlabel_align='right')

        return pie_chart_type

    def generatePieChart_phase(self) -> go.Figure:
        labels = ["سه فاز", "تک فاز"]
        pie_chart_phase = go.Figure(
            data=[go.Pie(labels=labels, values=[4000, 500],
                         title="سه فاز و تک فاز",
                         title_font_size=30,
                         hole=.3,
                         # pull=[0, 0, 0.2, 0.2],
                         marker_colors=["#4DCCAC", "#4DCC6D"],
                         # height=300,

                         )]
        )

        pie_chart_phase.update(layout_showlegend=False)
        pie_chart_phase.update_layout(
            margin=dict(t=20, l=0, r=0, b=0),
            paper_bgcolor="rgb(255,255,255)",  # "#ECEBEB",
            font_family="B Badr",
            font_size=20,
            height=300,

            # title={
            #     'text': "اولیه و ثانویه",
            #     # 'y': 0.9,
            #     # 'x': 0.5,
            #     'xanchor': 'center',
            #     # 'yanchor': 'top',
            #     'font_family': "B Badr",
            #     'font_size': 20,

            # }
        )

        pie_chart_phase.update_layout(
            hoverlabel=dict(
                # bgcolor="white",
                font_family="B Badr",
                font_size=20,
            ),
            hoverlabel_align='right')

        return pie_chart_phase
