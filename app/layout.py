import dash_bootstrap_components as dbc
from dash import html
from dash_ag_grid import AgGrid

from app.config import COLUMN_DEFS


def layout():
    return dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H1(
                                "Belgium Air Quality Data", className="text-center mb-4"
                            ),
                            dbc.Button(
                                "Refresh Data",
                                id="refresh-button",
                                color="primary",
                                className="mb-3",
                            ),
                            AgGrid(
                                id="data-table",
                                rowData=[],  # tol be populated by callback
                                columnDefs=COLUMN_DEFS,  # Define your column definitions based on your DynamoDB table structure
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
