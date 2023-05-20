from unittest.mock import ANY

from src.analysis_code.constants.types import ASTNodeType, StatementType
from src.analysis_code.tests.convert.base_convert import TestConverterBase, test_base


class TestConvert(TestConverterBase):
    @test_base
    def test_convert_import(self):
        self.sentence = "from random import randint"
        self.expected = {"type": str(ASTNodeType.IGNORE), "info": ANY, "indent": 0}

    @test_base
    def test_convert_def_function(self):
        self.sentence = "def quicksort(array):"
        self.expected = {
            "type": str(ASTNodeType.DEF),
            "info": dict(name="quicksort", args=["array"]),
        }

    @test_base
    def test_convert_return(self):
        self.sentence = "return array"
        self.expected = {
            "type": str(ASTNodeType.RETURN),
            "info": dict(name="array"),
        }

    @test_base
    def test_convert_return_statement(self):
        self.sentence = "return quicksort(low) + same + quicksort(high)"
        self.expected = {
            "type": str(ASTNodeType.RETURN),
            "info": dict(name="quicksort(low) + same + quicksort(high)"),
        }

    @test_base
    def test_convert_loop(self):
        self.sentence = "for item in array:"
        self.expected = {
            "type": str(ASTNodeType.LOOP),
            "info": dict(item="item", list="array"),
        }

    @test_base
    def test_convert_comment_hash(self):
        self.sentence = "# hello world"
        self.expected = {
            "type": str(ASTNodeType.COMMENT),
            "info": dict(value="hello world"),
        }

    @test_base
    def test_convert_statement_assign(self):
        self.sentence = "a = b"
        self.expected = {
            "type": str(ASTNodeType.STATEMENT),
            "info": dict(value="a = b", type=StatementType.ASSIGN.name),
        }

    @test_base
    def test_convert_statement_method(self):
        self.sentence = "a.append(b)"
        self.expected = {
            "type": str(ASTNodeType.STATEMENT),
            "info": dict(value="a.append(b)", type=StatementType.METHOD.name),
        }
