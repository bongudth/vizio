from unittest import TestCase

from src.analysis_code.decorators.code_reader_decorators import rule_response


class TestCaseDecorator(TestCase):
    @rule_response
    def handle_sentence(self, sentence: str):
        return {"value": sentence, "is_returned": True}

    def test_rule_response(self):
        line = "hello world"
        resp = self.handle_sentence(line)
        self.assertDictEqual(
            resp,
            {"value": line, "is_returned": True},
        )
