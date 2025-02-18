from datetime import datetime, timezone

import pandas as pd
import plotly.graph_objects as go
from dash import Input, Output

from app.config import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    MAP_CENTER,
    TABLE_NAME,
)
from app.data import DynamoDBTableHandler

db_handler = DynamoDBTableHandler(TABLE_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)


def register_callbacks(app):
    @app.callback(
        [Output("data-store", "data"), Output("last-update-time", "children")],
        Input("interval-component", "n_intervals"),
    )
    def update_store(n):
        items = db_handler.get_all_items()
        current_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S") + " UTC"
        return items, f"Last updated: {current_time}"

    @app.callback(Output("data-table", "rowData"), Input("data-store", "data"))
    def update_table(data):
        return data

    @app.callback(Output("map-plot", "figure"), Input("data-store", "data"))
    def update_map(data):
        df = pd.DataFrame(data)
        fig = go.Figure(
            data=[
                go.Scattermapbox(
                    lat=df["latitude"],
                    lon=df["longitude"],
                    mode="markers",
                    hovertemplate="<br>".join(
                        [
                            "City: %{customdata[0]}",
                            "Parameter: %{customdata[1]}",
                            "Value: %{customdata[2]}",
                            "Unit: %{customdata[3]}",
                        ]
                    ),
                    customdata=df[["city", "parameter", "value", "unit"]].values,
                )
            ],
            layout=go.Layout(
                mapbox=dict(
                    style="open-street-map",
                    zoom=6,
                    center=MAP_CENTER,
                ),
                height=400,
                margin={"r": 0, "t": 0, "l": 0, "b": 0},
                showlegend=False,
            ),
        )

        return fig
