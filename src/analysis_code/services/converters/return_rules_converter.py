from src.analysis_code.constants.types import ASTNodeType
from src.analysis_code.services.converters.base_rules_converter import (
    BaseRulesConverter,
)


class ReturnRulesConverter(BaseRulesConverter):
    KEYWORDS = ["return "]
    AST_NODE_TYPE = ASTNodeType.RETURN

    @classmethod
    def handle(cls, sentence):
        split_words = sentence.strip().split(" ")
        return {"name": " ".join(split_words[1:])}
