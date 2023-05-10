import re

from src.analysis_code.constants.types import ASTNodeType
from src.analysis_code.services.converters.base_rules_converter import (
    BaseRulesConverter,
)


class DefinitionRulesConverter(BaseRulesConverter):
    KEYWORDS = ["def "]
    AST_NODE_TYPE = ASTNodeType.DEF

    @classmethod
    def handle(cls, sentence):
        split_words = sentence.strip().split(" ")
        matched_words = re.findall(r"(\w+)", split_words[1])
        return {
            "name": matched_words[0],
            "args": matched_words[1:],
        }
