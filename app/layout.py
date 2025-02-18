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
                            html.H1(
                                "Belgium Air Quality Data", className="text-center mb-4"
                            ),
                            html.Div(
                                "Last updated: Never",
                                id="last-update-time",
                                className="text-muted mb-3",
                            ),
                        ]
                    )
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Graph(
                                id="map-plot",
                                style={"height": "400px"},
                                figure={
                                    "layout": {
                                        "mapbox": {
                                            "center": MAP_CENTER,
                                            "zoom": 6,
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
                            # TODO: add parent column city
                            AgGrid(
                                id="data-table",
                                rowData=[],
                                columnDefs=COLUMN_DEFS,
                                dashGridOptions={
                                    "pagination": True,
                                    "paginationAutoPageSize": True,
                                },
                                className="ag-theme-alpine",
                                style={"height": "400px", "width": "100%"},
                                columnSize="autoSize",
                            ),
                        ],
                        width=6,
                    ),
                ]
            ),
        ],
        fluid=True,
    )
