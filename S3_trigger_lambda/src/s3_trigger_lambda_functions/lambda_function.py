import json
from urllib.parse import unquote_plus

import boto3
from aws_lambda_powertools import Logger

logger = Logger()


def lambda_handler(event, context):
    logger.info(json.dumps(event))

    # バケット名
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    logger.info(bucket_name)

    # オブジェクトキー
    object_key = unquote_plus(event["Records"][0]["s3"]["object"]["key"])
    logger.info(object_key)

    # ETag
    etag = event["Records"][0]["s3"]["object"]["eTag"]
    logger.info(etag)

    # サイズ
    size = event["Records"][0]["s3"]["object"]["size"]
    logger.info(size)

    # S3にアップロードされたファイル内容を取得
    s3_client = boto3.client("s3")
    response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
    logger.info(response)
    file_content = response["Body"].read()
    logger.info(file_content)
