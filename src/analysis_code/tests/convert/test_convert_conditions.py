from src.analysis_code.constants.types import ASTNodeType, ConditionType
from src.test.analysis_code.convert.base_convert import TestConverterBase, test_base


class TestConvertConditions(TestConverterBase):
    @test_base
    def test_convert_conditional(self):
        self.sentence = "if len(array) < 2:"
        self.expected = {
            "type": str(ASTNodeType.CONDITIONS),
            "info": dict(type=str(ConditionType.IF), conditions=["len(array) < 2"]),
        }

    @test_base
    def test_convert_conditional_with_indent(self):
        self.sentence = "    if item < pivot:"
        self.expected = {
            "indent": 4,
            "type": str(ASTNodeType.CONDITIONS),
            "info": dict(type=str(ConditionType.IF), conditions=["item < pivot"]),
        }

    @test_base
    def test_convert_elif(self):
        self.sentence = "    elif item == pivot:"
        self.expected = {
            "indent": 4,
            "type": str(ASTNodeType.CONDITIONS),
            "info": dict(conditions=["item == pivot"], type=ConditionType.ELIF.name),
        }

    @test_base
    def test_convert_else(self):
        self.sentence = "else:"
        self.expected = {
            "type": str(ASTNodeType.CONDITIONS),
            "info": dict(type=str(ConditionType.ELSE)),
        }
