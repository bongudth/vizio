from src.analysis_code.constants.types import ASTNodeType, ConditionType
from src.analysis_code.services.converters.base_rules_converter import (
    BaseRulesConverter,
)


class ConditionRulesConverter(BaseRulesConverter):
    KEYWORDS = ["if ", "elif ", "else:"]
    AST_NODE_TYPE = ASTNodeType.CONDITIONS

    @classmethod
    def handle(cls, sentence):
        return cls.route(sentence=sentence)

    @classmethod
    def route(cls, sentence):
        sentence = sentence.rstrip()
        strip_sentence = sentence.strip()
        if strip_sentence.startswith("if"):
            return cls.handle_conditions_if(sentence)
        if strip_sentence.startswith("elif"):
            return cls.handle_conditions_elif(sentence)
        if strip_sentence.startswith("else"):
            return cls.handle_conditions_else(sentence)
        return dict(is_returned=False, info={})

    @classmethod
    def handle_conditions_if(cls, sentence):
        if sentence[-1] == ":":
            striped_sentence = sentence.strip()
            conditions = [striped_sentence[:-1].replace("if", "").strip()]
            return {"conditions": conditions, "type": ConditionType.IF.name}
        return None

    @classmethod
    def handle_conditions_elif(cls, sentence):
        if sentence[-1] == ":":
            striped_sentence = sentence.strip()
            conditions = [striped_sentence.replace("elif", "")[:-1].strip()]
            return {"conditions": conditions, "type": ConditionType.ELIF.name}
        return None

    @classmethod
    def handle_conditions_else(cls, sentence):
        if sentence[-1] == ":":
            return {"type": ConditionType.ELSE.name}
        return None
