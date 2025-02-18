import dash_bootstrap_components as dbc
from dash import dcc, html
from dash_ag_grid import AgGrid

from app.config import COLUMN_DEFS


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
                            AgGrid(
                                id="data-table",
                                rowData=[],  # to be populated by callback
                                columnDefs=COLUMN_DEFS,
                                dashGridOptions={
                                    "pagination": True,
                                    "paginationAutoPageSize": True,
                                },
                                className="ag-theme-alpine",
                                style={"height": "600px", "width": "100%"},
                                columnSize="autoSize",
                            ),
                        ]
                    )
                ]
            )
        ],
        fluid=True,
    )
