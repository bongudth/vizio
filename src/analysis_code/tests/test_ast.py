import ast
import json
import os
from unittest import TestCase

from src.analysis_code.services.visitors import PythonVisitor
from utils.file_handler import write_file


class TestPythonAst(TestCase):
    input_file = ""
    current_dir = os.path.abspath(os.path.dirname(__file__))  # src/analysis_code/tests
    input_dir = os.path.join(
        current_dir, "data/input"
    )  # src/analysis_code/tests/data/input
    output_dir = os.path.join(
        current_dir, "data/output"
    )  # src/analysis_code/tests/data/output
    output_ast_dir = os.path.join(
        output_dir, "ast"
    )  # src/analysis_code/tests/data/output/ast
    output_json_dir = os.path.join(
        output_dir, "json"
    )  # src/analysis_code/tests/data/output/json

    def test_ast(self):
        input_files = os.listdir(self.input_dir)  # ['test1.py', 'test2.py', 'test3.py']
        for input_file in input_files:
            self.input_file = input_file
            self._handle_ast()

    def _handle_ast(self):
        # Read file
        input_full_path = os.path.join(self.input_dir, self.input_file)
        output_ast_full_path = os.path.join(
            self.output_ast_dir, f"{self.input_file}.ast"
        )
        output_json_full_path = os.path.join(
            self.output_json_dir, f"{self.input_file}.json"
        )

        visitor = PythonVisitor()
        with open(input_full_path, "r") as f:
            content = f.read()
            tree = ast.parse(content)
        write_file(output_ast_full_path, ast.dump(tree, indent=4))

        # Append parent to each node
        for node in ast.walk(tree):
            for child in ast.iter_child_nodes(node):
                child.parent = node

        # Convert ast to json
        visitor.visit(tree)

        json_data = [node.to_dict() for node in visitor.output]
        output = json.dumps(json_data, indent=4)

        write_file(output_json_full_path, output)
