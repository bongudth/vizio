from unittest import TestCase
from unittest.mock import patch

from src.analysis_code.constants.types import ASTNodeType
from src.analysis_code.services.code_reader import CoderReader


class TestCoderReader(TestCase):
    # Tests that parse_file method returns expected results for valid file path.
    @patch("src.analysis_code.services.code_reader.read_file")
    def test_parse_file_valid_path(self, mock_read_file):
        # Setup
        file_path = "test_file.py"
        mock_read_file.return_value = ["def test():\n", "    print('hello')\n"]
        expected_result = [
            {
                "type": ASTNodeType.DEF.name,
                "info": {"name": "test", "args": []},
                "indent": 0,
            },
            {
                "type": ASTNodeType.STATEMENT.name,
                "info": {"type": "METHOD", "value": "print('hello')"},
                "indent": 4,
            },
        ]
        coder_reader = CoderReader()

        # Exercise
        result = coder_reader.parse_file(file_path)

        # Verify
        assert result == expected_result
        mock_read_file.assert_called_once_with(file_path)

    def test_parse_string_valid_code(self):
        # Setup
        source_code = "def test():\n    print('hello')\n"
        expected_result = [
            {
                "type": ASTNodeType.DEF.name,
                "info": {"name": "test", "args": []},
                "indent": 0,
            },
            {
                "type": ASTNodeType.STATEMENT.name,
                "info": {"type": "METHOD", "value": "print('hello')"},
                "indent": 4,
            },
        ]
        coder_reader = CoderReader()

        # Exercise
        result = coder_reader.parse_string(source_code)

        # Verify
        assert result == expected_result

    @patch("src.analysis_code.services.code_reader.read_file")
    def test_parse_lines_empty_path(self, mock_read_file):
        # Setup
        file_path = ""
        expected_result = []

        # Exercise
        coder_reader = CoderReader()
        result = coder_reader.parse_file(file_path)

        # Verify
        assert result == expected_result
