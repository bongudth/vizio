from unittest import TestCase

from src.draw_graph.services.dotfile_creator import DotfileCreator


class TestDrawFlowChart(TestCase):
    def test_draw_conditions(self):
        lines = [
            {
                "type": "CONDITIONS",
                "info": {"conditions": ["item == pivot"], "type": "IF"},
                "indent": 8,
            },
            {
                "type": "STATEMENT",
                "info": {"type": "METHOD", "value": "same.append(item)"},
                "indent": 12,
            },
        ]
        dot_file_creator = DotfileCreator(lines)
        content = dot_file_creator.generate()
        print(content)

    def test_draw_comments(self):
        lines = [
            {"type": "IGNORE", "info": {}, "indent": 0},
            {
                "type": "DEF",
                "info": {"name": "quicksort", "args": ["array"]},
                "indent": 0,
            },
            {
                "type": "COMMENT",
                "info": {
                    "value": "If the input array contains fewer than two elements,"
                },
                "indent": 4,
            },
            {
                "type": "COMMENT",
                "info": {"value": "then return it as the result of the function"},
                "indent": 4,
            },
            {
                "type": "CONDITIONS",
                "info": {"conditions": ["len(array) < 2"], "type": "IF"},
                "indent": 4,
            },
            {"type": "RETURN", "info": {"name": "array"}, "indent": 8},
        ]
        dot_file_creator = DotfileCreator(lines)
        dot_file_creator.generate()
