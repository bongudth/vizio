import ast
import os
from unittest import TestCase


class TestPythonAst(TestCase):
    input = "fibo.py"
    current_dir = os.path.abspath(os.path.dirname(__file__))
    test_analysis_code_dir = os.path.abspath(os.path.dirname(current_dir))
    test_data_dir = os.path.join(test_analysis_code_dir, "tests/data")

    def test_ast(self):
        full_path = os.path.join(self.test_data_dir, self.input)
        print(full_path)
        with open(full_path, "r") as f:
            content = f.read()
        tree = ast.parse(content)
        print(ast.dump(tree, indent=4))
