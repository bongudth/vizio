import traceback
import unittest
from typing import Callable
from unittest.mock import ANY

from src.analysis_code.constants.types import ASTNodeType
from src.analysis_code.services.code_reader import CoderReader
from src.logger.app_log import AppLog


def test_base(func: Callable):
    def wrapper(self):
        func(self)
        self.expected["indent"] = self.expected.get("indent") or 0
        try:
            response = self.code_reader.parse_line(self.sentence)
        except Exception as e:
            AppLog.error(f"Error parsing: {self.sentence}")
            AppLog.error(traceback.format_exc())
            raise e

        self.assertDictEqual(response, self.expected)

    return wrapper


class TestConverterBase(unittest.TestCase):
    def setUp(self):
        self.code_reader = CoderReader()

    @test_base
    def test_convert_base(self):
        self.sentence = "import abc"
        self.expected = {"type": str(ASTNodeType.IGNORE), "info": ANY, "indent": 0}
