import ast
import json
import os
from unittest import TestCase

from src.analysis_code.services.visitors import PythonVisitor
from utils.file_handler import write_file


class TestPythonAst(TestCase):
    input_file = "insertion_sort.py"
    current_dir = os.path.abspath(os.path.dirname(__file__))
    test_analysis_code_dir = os.path.abspath(os.path.dirname(current_dir))
    test_data_dir = os.path.join(test_analysis_code_dir, "tests/data")
    output_dir = os.path.join(test_data_dir, "output")

    def test_ast(self):
        input_files = [
            "if_else.py",
            "fibo.py",
            "insertion_sort.py",
            "node_connections.py",
            "bucket_sort.py",
            "counting_sort.py",
            "intersection.py",
            "lower_upper_decomposition.py",
            "quick_sort.py",
            "find_max.py",
            "secant_method.py",
            "shell_sort.py",
        ]
        for input_file in input_files:
            self.input_file = input_file
            self._handle_ast()

    def _handle_ast(self):
        # Read file
        full_path = os.path.join(self.test_data_dir, self.input_file)
        tree_ast_output_path = os.path.join(self.output_dir, f"{self.input_file}.ast")
        output_path = os.path.join(self.output_dir, f"{self.input_file}.json")

        visitor = PythonVisitor()
        with open(full_path, "r") as f:
            content = f.read()
            tree = ast.parse(content)
        write_file(tree_ast_output_path, ast.dump(tree, indent=4))

        # Append parent to each node
        for node in ast.walk(tree):
            for child in ast.iter_child_nodes(node):
                child.parent = node

        # Convert ast to json
        visitor.visit(tree)

        json_data = [node.to_dict() for node in visitor.output]
        output = json.dumps(json_data, indent=4)

        write_file(output_path, output)
