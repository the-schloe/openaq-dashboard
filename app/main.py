import dash_bootstrap_components as dbc
from dash import Dash

from app.callbacks import register_callbacks
from app.layout import layout

app = Dash(
    __name__, external_stylesheets=[dbc.themes.MINTY], title="Air Quality Dashboard"
)
app.layout = layout

register_callbacks(app)

server = app.server
if __name__ == "__main__":
    app.run_server(debug=True, port=8080)
