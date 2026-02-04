import boto3

def get_s3_client(region="eu-west-1"):
    return boto3.client("s3", region_name=region)


def get_sqs_client(region="eu-west-1"):
    return boto3.client("sqs", region_name=region)


