from datetime import datetime, timezone

import pandas as pd
import plotly.graph_objects as go
from dash import Input, Output

from app.config import (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, MAP_CENTER,
                        TABLE_NAME)
from app.data import DynamoDBTableHandler

db_handler = DynamoDBTableHandler(TABLE_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)


def register_callbacks(app):
    @app.callback(
        [Output("data-store", "data"), Output("last-update-time", "children")],
        [
            Input("interval-component", "n_intervals"),
            Input("aggregation-type", "value"),
            Input("time-window", "value"),
        ],
    )
    def update_store(n, aggregation_type, time_window):
        hours = int(time_window)
        df = db_handler.get_aggregated_items(hours=hours, aggregation=aggregation_type)
        current_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S") + " UTC"
        # Note: store needs json serializable data, so we convert the dataframe to a list of dictionaries
        return df.to_dict("records"), f"Last updated: {current_time}"

    @app.callback(Output("data-table", "rowData"), Input("data-store", "data"))
    def update_table(data):
        return data

    @app.callback(Output("map-plot", "figure"), Input("data-store", "data"))
    def update_map(data):
        df = pd.DataFrame(data)
        if df.empty:
            df = pd.DataFrame(
                columns=["city", "parameter", "unit", "latitude", "longitude", "value"]
            )
        # TODO: remove tooltip trace name
        # TODO: combine parameters into one trace
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
                    zoom=7,
                    center=MAP_CENTER,
                ),
                height=400,
                margin={"r": 0, "t": 0, "l": 0, "b": 0},
                showlegend=False,
            ),
        )
        if df.empty:
            fig.add_annotation(
                text="No data!",
                x=0.5,
                y=0.5,
                xref="paper",
                yref="paper",
                showarrow=False,
                font=dict(size=50),
            )
        return fig
