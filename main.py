import json
import logging

from src.service import generate_dot

logger = logging.getLogger(__name__)


def lambda_handler(event, context):
    try:
        body = validate_value(event)
        source_code = body.get("source_code", None)
        body.get("output_type", "svg")
        logger.info("Source code: %s", source_code)
        content = generate_dot(source_code)
        return {"statusCode": 200, "body": json.dumps({"results": content})}
    except Exception as e:
        logging.error(e, exc_info=True)
        return {"statusCode": 500, "body": json.dumps(str(e))}


def validate_value(event):
    body = event.get("body", None)
    return json.loads(body)
