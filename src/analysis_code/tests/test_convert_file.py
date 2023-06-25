import os
from unittest import TestCase, skip

from src.analysis_code.services.code_reader import CoderReader
from src.utils.file_handler import write_file


@skip("Skip this test")
class TestConvertFile(TestCase):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    filenames = [
        "fibo.py",
        "node_connections.py",
        "quick_sort.py",
    ]

    def setUp(self) -> None:
        self.code_reader = CoderReader()

    def test_write_file(self):
        for filename in self.filenames:
            file_path = os.path.abspath(
                os.path.join(self.current_dir, "data", filename)
            )
            results = self.code_reader.parse_file(file_path)
            output = os.path.abspath(
                os.path.join(self.current_dir, "data/output", f"output_{filename}.txt")
            )
            write_file(output, "\n".join([str(result) for result in results]))
