from unittest import TestCase

from src.analysis_code.models.ac_node import ACNode


class TestCaseACNodes(TestCase):
    def test_ac_node_from_dict(self):
        data = {
            "type": "STATEMENT",
            "info": {
                "type": "STATEMENT_ASSIGN",
                "value": "pivot = array[randint(0, len(array) - 1)]",
            },
            "indent": 4,
        }
        node = ACNode().from_dict(data)
        assert node.to_dict() == data
