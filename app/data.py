from datetime import datetime, timedelta, timezone

import boto3
import pandas as pd


class DynamoDBTableHandler:
    def __init__(
        self,
        table_name: str,
        aws_access_key_id: str,
        aws_secret_access_key: str,
        region_name: str = "eu-west-1",
    ):
        self.dynamodb = boto3.resource(
            "dynamodb",
            region_name=region_name,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )
        self.table = self.dynamodb.Table(table_name)

    def _get_all_items(self, hours: int = 3) -> list[dict]:
        now = datetime.now(timezone.utc)
        n_hours_ago = now - timedelta(hours=hours)

        items = []
        last_evaluated_key = None

        while True:
            scan_kwargs = {
                "FilterExpression": "#ts >= :min_ts",
                "ExpressionAttributeNames": {"#ts": "timestamp"},
                "ExpressionAttributeValues": {
                    ":min_ts": n_hours_ago.strftime("%Y-%m-%d %H:%M:%S.%f")
                },
            }

            if last_evaluated_key:
                scan_kwargs["ExclusiveStartKey"] = last_evaluated_key

            response = self.table.scan(**scan_kwargs)
            items.extend(response.get("Items", []))

            last_evaluated_key = response.get("LastEvaluatedKey")
            if not last_evaluated_key:
                break
        return items

    def get_aggregated_items(
        self, hours: int = 3, aggregation: str = "maximum"
    ) -> pd.DataFrame:
        items = self._get_all_items(hours=hours)

        df = pd.DataFrame(items)
        if df.empty:
            return pd.DataFrame(
                columns=["city", "parameter", "unit", "latitude", "longitude", "value"]
            )

        df["latitude"] = df["latitude"].astype(float)
        df["longitude"] = df["longitude"].astype(float)
        df["value"] = df["value"].astype(float)

        cols_to_keep = ["city", "parameter", "unit", "latitude", "longitude"]

        counts = df.groupby(cols_to_keep).size().reset_index(name="count")

        if aggregation == "maximum":
            df = df.groupby(cols_to_keep)["value"].max().reset_index()
        elif aggregation == "minimum":
            df = df.groupby(cols_to_keep)["value"].min().reset_index()
        elif aggregation == "average":
            df = df.groupby(cols_to_keep)["value"].mean().reset_index()
        else:
            raise ValueError(f"Invalid aggregation type: {aggregation}")

        df = df.merge(counts, on=cols_to_keep)
        return df
