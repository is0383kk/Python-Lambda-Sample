from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from lambda_function import router as dynamo_router

logger = Logger()

# API Gatewayのリクエストを処理するためのアプリケーションを定義
app = APIGatewayRestResolver()
# 外部定義されたルーター (dynamo_router) をアプリケーションに追加
app.include_router(dynamo_router)


@logger.inject_lambda_context(log_event=True)
def lambda_handler(event, context):
    # API Gatewayからのリクエストを解決して応答を返す
    return app.resolve(event, context)
