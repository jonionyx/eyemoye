import json

def fetch_events_from_s3(bucket, prefix, s3_client):
    """
    Fetch raw JSON events from S3 (e.g. event-store / firehose output)
    """
    events = []

    response = s3_client.list_objects_v2(
        Bucket=bucket,
        Prefix=prefix
    )

    for obj in response.get("Contents", []):
        body = s3_client.get_object(
            Bucket=bucket,
            Key=obj["Key"]
        )["Body"].read()

        events.append(json.loads(body))

    return events
