import dash_bootstrap_components as dbc
from dash import dcc, html
from dash_ag_grid import AgGrid

from app.config import COLUMN_DEFS, MAP_CENTER, UPDATE_RATE


def layout():
    return dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Interval(
                                id="interval-component",
                                interval=UPDATE_RATE,
                                n_intervals=0,
                            ),
                            dcc.Loading(
                                id="store-loading",
                                color="darkslateblue",
                                children=[dcc.Store(id="data-store")],
                                type="default",
                                className="m-4",
                            ),
                        ]
                    )
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H4(
                                [
                                    html.Div(
                                        [
                                            dcc.Dropdown(
                                                id="aggregation-type",
                                                options=[
                                                    {
                                                        "label": "Maximum",
                                                        "value": "maximum",
                                                    },
                                                    {
                                                        "label": "Minimum",
                                                        "value": "minimum",
                                                    },
                                                    {
                                                        "label": "Average",
                                                        "value": "average",
                                                    },
                                                ],
                                                value="average",
                                                style={
                                                    "width": "150px",
                                                    "display": "inline-block",
                                                },
                                            ),
                                            html.Span(
                                                " air quality measurements within the last ",
                                                style={"margin": "0 10px"},
                                            ),
                                            dcc.Dropdown(
                                                id="time-window",
                                                options=[
                                                    {"label": "3", "value": "3"},
                                                    {"label": "6", "value": "6"},
                                                    {"label": "12", "value": "12"},
                                                    {"label": "24", "value": "24"},
                                                ],
                                                value="3",
                                                style={
                                                    "width": "50px",
                                                    "display": "inline-block",
                                                },
                                            ),
                                            html.Span(
                                                " hours", style={"margin-left": "10px"}
                                            ),
                                        ],
                                        style={
                                            "display": "inline-flex",
                                            "alignItems": "center",
                                        },
                                    ),
                                ],
                                className="text-center m-4",
                            ),
                        ],
                    ),
                ],
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Loading(
                                id="loading-map",
                                color="darkslateblue",
                                children=[
                                    dcc.Graph(
                                        id="map-plot",
                                        style={
                                            "height": "600px",
                                            "borderRadius": "9px",
                                            "overflow": "hidden",
                                        },
                                        figure={
                                            "layout": {
                                                "map": {
                                                    "center": MAP_CENTER,
                                                    "zoom": 7,
                                                    "style": "dark",
                                                },
                                                "margin": {
                                                    "r": 0,
                                                    "t": 0,
                                                    "l": 0,
                                                    "b": 0,
                                                },
                                                "xaxis": {"visible": False},
                                                "yaxis": {"visible": False},
                                                "paper_bgcolor": "#182230",
                                                "plot_bgcolor": "#182230",
                                            }
                                        },
                                        config={
                                            "scrollZoom": True,
                                            "displayModeBar": False,
                                        },
                                    )
                                ],
                            )
                        ],
                        width=6,
                        className="mb-4",
                    ),
                    dbc.Col(
                        [
                            dcc.Loading(
                                id="loading-table",
                                type="default",
                                color="darkslateblue",
                                children=[
                                    AgGrid(
                                        id="data-table",
                                        rowData=[],
                                        columnDefs=COLUMN_DEFS,
                                        dashGridOptions={
                                            "pagination": True,
                                            "paginationAutoPageSize": True,
                                        },
                                        className="ag-theme-quartz-dark",
                                        style={
                                            "height": "600px",
                                            "width": "100%",
                                            "borderRadius": "9px",
                                        },
                                    ),
                                ],
                            )
                        ],
                        width=6,
                    ),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Div(
                                "Last updated: Never",
                                id="last-update-time",
                                className="text-muted text-end",
                            ),
                        ],
                        width=12,
                    ),
                ],
                className="mt-3",
            ),
        ],
        fluid=True,
    )
