from dash import Input, Output
from datetime import datetime, timezone

from app.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, TABLE_NAME
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
