from src.analysis_code.constants.types import ASTNodeType
from src.analysis_code.services.converters.base_rules_converter import (
    BaseRulesConverter,
)


class ImportRulesConverter(BaseRulesConverter):
    KEYWORDS = ["import ", "from "]
    AST_NODE_TYPE = ASTNodeType.IGNORE

    @classmethod
    def handle(cls, sentence: str):
        return {"value": sentence.strip()}
