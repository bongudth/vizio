from typing import Any, Dict

from src.analysis_code.constants.types import ASTNodeType, StatementType
from src.analysis_code.services.converters.base_rules_converter import (
    BaseRulesConverter,
)


class StatementAssignRulesConverter(BaseRulesConverter):
    KEYWORDS = ["="]
    AST_NODE_TYPE = ASTNodeType.STATEMENT

    @classmethod
    def can_handle(cls, sentence):
        return any(sentence.find(keyword) != -1 for keyword in cls.KEYWORDS)

    @classmethod
    def handle(cls, sentence: str) -> Dict[str, Any]:
        return {
            "type": StatementType.ASSIGN.name,
            "value": sentence.strip(),
        }
