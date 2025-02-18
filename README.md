# Air Quality Dashboard

A real-time dashboard displaying air quality measurements.

## Features

- Interactive map showing measurement locations
- Data table with detailed readings
- Configurable time window (3-24 hours)
- Multiple aggregation options (maximum, minimum, average)
- Auto-refresh every 10 seconds

## Prerequisites

- Python 3.12
- AWS credentials with DynamoDB access
- Required Python packages
    - install via `pip install -r requirements.txt`

## Environment Variables

Create a `.env` file with:

```
TABLE_NAME=your_dynamodb_table_name
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
```

## Running the app

```
docker compose up --build
```

## Accessing the app

Open your browser and navigate to `http://localhost:8080`
