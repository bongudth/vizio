import json
import logging

from src.service import generate_dot, generate_dot_v2

logger = logging.getLogger(__name__)


def lambda_handler(event, context):
    try:
        body = validate_value(event)
        source_code = body.get("source_code", None)
        body.get("output_type", "svg")
        logger.info("Source code: %s", source_code)
        content = generate_dot_v2(source_code)
        return {"statusCode": 200, "body": json.dumps({"results": content})}
    except Exception as e:
        logging.error(e, exc_info=True)
        return {"statusCode": 500, "body": json.dumps(str(e))}


def validate_value(event):
    body = event.get("body", None)
    return json.loads(body)


if __name__ == "__main__":
    event = {
        "body": json.dumps(
            {
                "source_code": """
def generate_dot(source_code: str):
    if not source_code:
        raise ValueError("source_code is required!")
"""
            }
        )
    }
    print(lambda_handler(event, None))
