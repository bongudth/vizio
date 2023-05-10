import ast
import os
from unittest import TestCase

from src.utils.file_handler import read_file, write_file


class TestPythonAst(TestCase):
    def test_ast(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(current_dir, "data/input/quick_sort.py")
        code = read_file(file_path)
        des_path = os.path.join(current_dir, "data/output/quick_sort.ast.txt")
        tree = ast.parse(code)
        write_file(des_path, ast.dump(tree, indent=4))
