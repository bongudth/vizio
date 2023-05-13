import os
from unittest import TestCase

from src.analysis_code.services.code_reader import CoderReader
from src.utils.file_handler import write_file


class TestConvertFile(TestCase):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    filename = "quick_sort" + ".py"

    @classmethod
    def setUpClass(cls) -> None:
        cls.file_path = os.path.abspath(
            os.path.join(cls.current_dir, "data/input", cls.filename)
        )

    def setUp(self) -> None:
        self.code_reader = CoderReader()

    def test_convert_file(self):
        self.code_reader.parse_file(self.file_path)

    def test_write_file(self):
        results = self.code_reader.parse_file(self.file_path)
        output = os.path.abspath(
            os.path.join(self.current_dir, "data/output", f"{self.filename}.txt")
        )
        write_file(output, "\n".join([str(result) for result in results]))
