import json
import logging

from src.service import generate_dot_v2

logger = logging.getLogger(__name__)


def lambda_handler(event, context):
    try:
        body = validate_value(event)
        source_code = body.get("source_code", None)
        need_summary = body.get("need_summary", False)
        if need_summary:
            content = generate_dot_v2(source_code, need_summary)
            return {"statusCode": 200, "body": json.dumps({"results": content})}

        logger.info("Source code: %s", source_code)
        content = generate_dot_v2(source_code)
        return {"statusCode": 200, "body": json.dumps({"results": content})}
    except Exception as e:
        logging.error(e, exc_info=True)
        return {"statusCode": 500, "body": json.dumps(str(e))}


def validate_value(event):
    body = event.get("body", None)
    return json.loads(body)


def test_generate_dot():
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


def test_summary_code():
    event = {
        "body": json.dumps(
            {
                "source_code": """
def handle_block_lines(self, lines: List[str], line: str, line_no: int):
    result = []
    pair_characters = [("(", ")"), ("[", "]"), ("{", "}")]
    indent = len(line) - len(line.lstrip(" "))
    last_char = line.rstrip()[-1] if line.rstrip() else ""
    for pair_character in pair_characters:
        if line.rstrip() and last_char == pair_character[0]:
            block_lines = []
            start_line_no = line_no
            while line.rstrip() and line_no <= len(lines):
                line = lines[line_no - 1]
                block_lines.append(line)
                if line.rstrip()[-1] == pair_character[1]:
                    break

                line_no += 1

            if block_lines:
                result.append(
                    {
                        "type": ASTNodeType.STATEMENT.name,
                        "info": {
                            "type": "BLOCK",
                        },
                        "indent": indent,
                        "line_no": start_line_no,
                    }
                )
    return result, line_no
""",
                "need_summary": True,
            }
        )
    }
    print(lambda_handler(event, None))


if __name__ == "__main__":
    # test_generate_dot()
    test_summary_code()
