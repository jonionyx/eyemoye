import json

def fetch_events_from_sqs(queue_url, sqs_client, max_messages=10):
    """
    Fetch messages from SQS without deleting them
    """
    events = []

    response = sqs_client.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=max_messages,
        WaitTimeSeconds=5
    )

    for msg in response.get("Messages", []):
        events.append(json.loads(msg["Body"]))

    return events
