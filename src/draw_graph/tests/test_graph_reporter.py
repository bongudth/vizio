from unittest import TestCase

from src.draw_graph.services.dotfile_creator import DotfileCreator


class TestGraphReporter(TestCase):
    def test_graph_reporter(self):
        lines = [
            {
                "type": "CONDITIONS",
                "info": {"conditions": ["item == pivot"], "type": "IF"},
                "indent": 8,
            },
            {
                "type": "STATEMENT",
                "info": {"type": "STATEMENT_METHOD", "value": "same.append(item)"},
                "indent": 12,
            },
        ]
        dot_file_creator = DotfileCreator(lines)
        dot_file_creator.generate()
