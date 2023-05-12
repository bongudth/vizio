import os
from unittest import TestCase

from src.draw_graph.services.dotfile_creator import DotfileCreator
from src.utils.file_handler import read_file, write_file


class TestDrawFlowChart(TestCase):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_dir = os.path.join(current_dir, "data/input")
    output_dir = os.path.join(current_dir, "data/output")

    def __write_dotfile(self, origin_file_name: str):
        full_path = os.path.join(self.input_dir, origin_file_name)
        dot_full_path = os.path.join(self.output_dir, f"{origin_file_name}.dot")
        lines = read_file(full_path)
        dot_file_creator = DotfileCreator(lines)
        content = dot_file_creator.generate()
        print(content)
        write_file(dot_full_path, content)
        svg_full_path = dot_full_path.replace(".dot", ".svg")
        os.system(f"dot -Tsvg {dot_full_path} -o {svg_full_path}")

    def test_draw_quick_sort(self):
        self.__write_dotfile("quick_sort.py")

    def test_draw_conditions(self):
        path = os.path.join(self.output_dir, "test_conditions.dot")
        lines = [
            {
                "type": "STATEMENT",
                "info": {
                    "type": "STATEMENT_ASSIGN",
                    "value": "pivot = array[randint(0, len(array) - 1)]",
                },
                "indent": 4,
            },
            {"type": "LOOP", "info": {"item": "item", "list": "array"}, "indent": 4},
            {
                "type": "CONDITIONS",
                "info": {"conditions": ["item < pivot"], "type": "IF"},
                "indent": 8,
            },
            {
                "type": "STATEMENT",
                "info": {"type": "STATEMENT_METHOD", "value": "low.append(item)"},
                "indent": 12,
            },
            {
                "type": "CONDITIONS",
                "info": {"conditions": ["item == pivot"], "type": "ELIF"},
                "indent": 8,
            },
            {
                "type": "STATEMENT",
                "info": {"type": "STATEMENT_METHOD", "value": "same.append(item)"},
                "indent": 12,
            },
            {
                "type": "CONDITIONS",
                "info": {"conditions": ["item > pivot"], "type": "ELIF"},
                "indent": 8,
            },
            {
                "type": "STATEMENT",
                "info": {"type": "STATEMENT_METHOD", "value": "high.append(item)"},
                "indent": 12,
            },
            {
                "type": "RETURN",
                "info": {"name": "quicksort(low) + same + quicksort(high)"},
                "indent": 4,
            },
        ]
        dot_file_creator = DotfileCreator(lines)
        content = dot_file_creator.generate()
        write_file(path, content)

    def test_flow_chart_condition(self):
        path = os.path.join(self.output_dir, "test_flow_chart_conditions.dot")
        lines = [
            {
                "type": "CONDITIONS",
                "info": {"conditions": ["len(array) < 2"], "type": "IF"},
                "indent": 4,
            },
            {"type": "RETURN", "info": {"name": "array"}, "indent": 8},
            {
                "type": "STATEMENT",
                "info": {
                    "type": "STATEMENT_ASSIGN",
                    "value": "low, same, high = [], [], []",
                },
                "indent": 4,
            },
            {
                "type": "STATEMENT",
                "info": {
                    "type": "STATEMENT_ASSIGN",
                    "value": "pivot = array[randint(0, len(array) - 1)]",
                },
                "indent": 4,
            },
        ]
        dot_file_creator = DotfileCreator(lines)
        content = dot_file_creator.generate()
        print(content)
        write_file(path, content)
        report = dot_file_creator.get_report()
        self.assertEqual(report.get("n_nodes"), 6)
        self.assertEqual(report.get("n_connections"), 6)
