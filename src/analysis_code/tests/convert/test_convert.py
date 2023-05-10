from unittest.mock import ANY

from src.analysis_code.constants.types import ASTNodeType, StatementType
from src.analysis_code.tests.convert.base_convert import TestConverterBase, base_convert


class TestConvert(TestConverterBase):
    @base_convert
    def test_convert_import(self):
        self.sentence = "from random import randint"
        self.expected = {"type": str(ASTNodeType.IGNORE), "info": ANY, "indent": 0}

    @base_convert
    def test_convert_def_function(self):
        self.sentence = "def quicksort(array):"
        self.expected = {
            "type": str(ASTNodeType.DEF),
            "info": {"name": "quicksort", "args": ["array"]},
        }

    @base_convert
    def test_convert_return(self):
        self.sentence = "return array"
        self.expected = {
            "type": str(ASTNodeType.RETURN),
            "info": {"name": "array"},
        }

    @base_convert
    def test_convert_return_statement(self):
        self.sentence = "return quicksort(low) + same + quicksort(high)"
        self.expected = {
            "type": str(ASTNodeType.RETURN),
            "info": {"name": "quicksort(low) + same + quicksort(high)"},
        }

    @base_convert
    def test_convert_loop(self):
        self.sentence = "for item in array:"
        self.expected = {
            "type": str(ASTNodeType.LOOP),
            "info": {"item": "item", "list": "array"},
        }

    @base_convert
    def test_convert_comment_hash(self):
        self.sentence = "# hello world"
        self.expected = {
            "type": str(ASTNodeType.COMMENT),
            "info": {"value": "hello world"},
        }

    @base_convert
    def test_convert_statement_assign(self):
        self.sentence = "a = b"
        self.expected = {
            "type": str(ASTNodeType.STATEMENT),
            "info": {"value": "a = b", "type": str(StatementType.STATEMENT_ASSIGN)},
        }

    @base_convert
    def test_convert_statement_method(self):
        self.sentence = "a.append(b)"
        self.expected = {
            "type": str(ASTNodeType.STATEMENT),
            "info": {
                "value": "a.append(b)",
                "type": str(StatementType.STATEMENT_METHOD),
            },
        }
