from typing import Any, Dict

from src.analysis_code.constants.types import ASTNodeType
from src.analysis_code.services.converters.base_rules_converter import (
    BaseRulesConverter,
)


class LoopRulesConverter(BaseRulesConverter):
    KEYWORDS = ["for ", "while "]
    AST_NODE_TYPE = ASTNodeType.LOOP

    @classmethod
    def handle(cls, sentence: str) -> Dict[str, Any]:
        split_words = sentence.strip().split(" ")
        item = split_words[1]
        item_list = " ".join(split_words[3:])[:-1]
        return {"item": item, "list": item_list}
