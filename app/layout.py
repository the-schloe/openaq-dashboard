import dash_bootstrap_components as dbc
from dash import dcc, html
from dash_ag_grid import AgGrid

from app.config import COLUMN_DEFS, MAP_CENTER


def layout():
    return dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Store(id="data-store"),
                            dcc.Interval(
                                id="interval-component",
                                interval=10 * 1000,
                                n_intervals=0,
                            ),
                            html.H1("Air Quality Data", className="text-center m-2"),
                            html.Hr(className="mb-4"),
                        ]
                    )
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Div(
                                [
                                    dcc.Dropdown(
                                        id="aggregation-type",
                                        options=[
                                            {"label": "Maximum", "value": "maximum"},
                                            {"label": "Minimum", "value": "minimum"},
                                            {"label": "Average", "value": "average"},
                                        ],
                                        value="average",
                                        style={
                                            "width": "100px",
                                            "display": "inline-block",
                                        },
                                    ),
                                    html.Span(
                                        " values within the last ",
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
                                    html.Span(" hours.", style={"margin-left": "10px"}),
                                ],
                                style={
                                    "textAlign": "center",
                                    "display": "flex",
                                    "justifyContent": "center",
                                    "alignItems": "center",
                                },
                            ),
                        ],
                    ),
                ],
            ),
            html.Hr(className="mb-4"),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Graph(
                                id="map-plot",
                                style={"height": "600px"},
                                figure={
                                    "layout": {
                                        "mapbox": {
                                            "center": MAP_CENTER,
                                            "zoom": 7,
                                            "style": "open-street-map",
                                        },
                                        "margin": {"r": 0, "t": 0, "l": 0, "b": 0},
                                    }
                                },
                                config={"scrollZoom": True, "displayModeBar": False},
                            )
                        ],
                        width=6,
                        className="mb-4",
                    ),
                    dbc.Col(
                        [
                            AgGrid(
                                id="data-table",
                                rowData=[],
                                defaultColDef=COLUMN_DEFS,
                                columnDefs=COLUMN_DEFS,
                                dashGridOptions={
                                    "pagination": True,
                                    "paginationAutoPageSize": True,
                                },
                                className="ag-theme-alpine",
                                style={"height": "600px", "width": "100%"},
                            ),
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
