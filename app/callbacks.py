from dash import Input, Output

from app.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, TABLE_NAME
from app.data import DynamoDBTableHandler

db_handler = DynamoDBTableHandler(TABLE_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)


def register_callbacks(app):
    @app.callback(Output("data-table", "rowData"), Input("refresh-button", "n_clicks"))
    def update_table(n_clicks):
        items = db_handler.get_all_items()
        return items
