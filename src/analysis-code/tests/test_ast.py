import ast
import os
from unittest import TestCase

from src.utils.file_handler import read_file, write_file


class TestFileHandler(TestCase):
    def test_file_handler(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(current_dir, "data/input/quick_sort.py")
        lines = read_file(file_path)
        tree = ast.parse(lines)
        des_path = os.path.join(current_dir, "data/output/quick_sort.ast.txt")
        write_file(des_path, ast.dump(tree, indent=4))
