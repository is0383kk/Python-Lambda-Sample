import json
import os
import uuid
import boto3
from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler.api_gateway import Response, Router

router = Router()
logger = Logger()


@router.post("/data/<user_id>")
def post_data(user_id):
    # boto3クライアントを定義
    dynamo_client = boto3.client("dynamodb")

    # 登録先のテーブル名をtemplate.yamlから取得
    table_name = os.getenv("DYNAMO_TABLE_NAME")

    # API呼び出し時のbody内容を取得
    body = router.current_event.json_body
    logger.info(body)

    # DynamoDBに登録するdynamo_idを発番
    dynamo_id = str(uuid.uuid4())

    # DynamoDBの登録先テーブルと登録データを定義
    params = {
        "TableName": table_name,
        "Item": {
            "dynamo_id": {"S": dynamo_id},
            "user_id": {"S": user_id},
            "name": {"S": body["name"]},
        },
    }
    try:
        # DynamoDBへの登録処理
        data = dynamo_client.put_item(**params)

        # 正常時はステータスコードを200とし処理結果を返す
        return Response(
            status_code=200,
            body=json.dumps(data),
            content_type="application/json"
        )
    except Exception as e:
        # エラー時はステータスコードを500としエラーメッセージを返す
        return Response(
            status_code=500,
            body={"error": str(e)},
            content_type="application/json",
        )