import os

from dotenv import load_dotenv

load_dotenv()

TABLE_NAME = os.getenv("TABLE_NAME")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

UPDATE_RATE = 60 * 1000  # 60 seconds
MAP_CENTER = {"lat": 50.5303, "lon": 4.3517}

COLUMN_DEFS = [
    {"headerName": "City", "field": "city", "width": 200},
    {"headerName": "Parameter", "field": "parameter", "width": 100},
    {"headerName": "Unit", "field": "unit", "width": 100},
    {
        "headerName": "Value",
        "field": "value",
        "width": 100,
        "cellDataType": "number",
        "valueFormatter": {"function": """d3.format(",.2f")(params.value)"""},
    },
    {
        "headerName": "Records",
        "field": "count",
        "width": 100,
        "cellDataType": "number",
    },
]
