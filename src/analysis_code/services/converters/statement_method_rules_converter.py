from typing import Any, Dict

from src.analysis_code.constants.types import ASTNodeType, StatementType
from src.analysis_code.services.converters.base_rules_converter import (
    BaseRulesConverter,
)


class StatementMethodRulesConverter(BaseRulesConverter):
    AST_NODE_TYPE = ASTNodeType.STATEMENT

    @classmethod
    def can_handle(cls, sentence):
        return "(" in sentence

    @classmethod
    def handle(cls, sentence: str) -> Dict[str, Any]:
        return {
            "type": str(StatementType.STATEMENT_METHOD),
            "value": sentence.strip(),
        }
