from src.analysis_code.constants.types import ASTNodeType, ConditionType
from src.analysis_code.tests.convert.base_convert import TestConverterBase, base_convert


class TestConvertConditions(TestConverterBase):
    @base_convert
    def test_convert_conditional(self):
        self.sentence = "if len(array) < 2:"
        self.expected = {
            "type": str(ASTNodeType.CONDITIONS),
            "info": {"type": str(ConditionType.IF), "conditions": ["len(array) < 2"]},
        }

    @base_convert
    def test_convert_conditional_with_indent(self):
        self.sentence = "    if item < pivot:"
        self.expected = {
            "indent": 4,
            "type": str(ASTNodeType.CONDITIONS),
            "info": {"type": str(ConditionType.IF), "conditions": ["item < pivot"]},
        }

    @base_convert
    def test_convert_elif(self):
        self.sentence = "    elif item == pivot:"
        self.expected = {
            "indent": 4,
            "type": str(ASTNodeType.CONDITIONS),
            "info": {"conditions": ["item == pivot"], "type": ConditionType.ELIF.name},
        }

    @base_convert
    def test_convert_else(self):
        self.sentence = "else:"
        self.expected = {
            "type": str(ASTNodeType.CONDITIONS),
            "info": {"type": str(ConditionType.ELSE)},
        }
