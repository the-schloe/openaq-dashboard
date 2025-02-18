import os

from dotenv import load_dotenv

load_dotenv()

TABLE_NAME = os.getenv("TABLE_NAME")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

# Center coordinates for Belgium
MAP_CENTER = {"lat": 50.8503, "lon": 4.3517}

COLUMN_DEFS = [
    {"headerName": "City", "field": "city"},
    {"headerName": "Parameter", "field": "parameter"},
    {"headerName": "Unit", "field": "unit"},
    {"headerName": "Value", "field": "value"},
]
