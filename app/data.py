from datetime import datetime, timedelta, timezone

import boto3


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

    def get_all_items(self) -> list[dict]:
        now = datetime.now(timezone.utc)
        n_hours_ago = now - timedelta(hours=12)

        response = self.table.scan(
            FilterExpression="#ts >= :min_ts",
            ExpressionAttributeNames={"#ts": "timestamp"},
            ExpressionAttributeValues={":min_ts": n_hours_ago.isoformat()},
        )
        items = response.get("Items", [])
        return items
