from typing import Any, Dict

from src.analysis_code.constants.types import ASTNodeType
from src.analysis_code.services.converters.base_rules_converter import (
    BaseRulesConverter,
)


class CommentRulesConverter(BaseRulesConverter):
    KEYWORDS = ["#"]
    AST_NODE_TYPE = ASTNodeType.COMMENT

    @classmethod
    def handle(cls, sentence: str) -> Dict[str, Any]:
        sentence = sentence.strip()
        return {
            "value": sentence[1:].strip(),
        }
