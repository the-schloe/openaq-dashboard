import dash_bootstrap_components as dbc
from dash import Dash

from app.callbacks import register_callbacks
from app.layout import layout

app = Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.SLATE,
        "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css",
    ],
    title="Air Quality Dashboard",
)
app.layout = layout

register_callbacks(app)

server = app.server
if __name__ == "__main__":
    app.run_server(debug=True, port=8080)
