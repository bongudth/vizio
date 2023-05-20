from unittest import TestCase

from src.analysis_code.models.ac_node import ACNode
from src.draw_graph.constants.node_types import NodeType
from src.draw_graph.services.dg_graph import DGGraph


class TestDGGraph(TestCase):
    # Tests that the function correctly merges consecutive statement/comment nodes with the same indent level and returns a DGNode with the concatenated label.
    def test_merge_consecutive_statement_nodes_happy(self):
        # Arrange
        nodes = [
            ACNode().from_dict(
                {
                    "type": "STATEMENT",
                    "info": {"type": "ASSIGN", "value": "a = 1"},
                    "indent": 0,
                }
            ),
            ACNode().from_dict(
                {"type": "COMMENT", "info": {"value": "This is a comment"}, "indent": 0}
            ),
            ACNode().from_dict(
                {
                    "type": "STATEMENT",
                    "info": {"type": "ASSIGN", "value": "b = 2"},
                    "indent": 0,
                }
            ),
            ACNode().from_dict(
                {
                    "type": "STATEMENT",
                    "info": {"type": "ASSIGN", "value": "c = 3"},
                    "indent": 0,
                }
            ),
        ]
        node = nodes[0]
        idx = 0
        expected_label = "a = 1\nb = 2\nc = 3\n"

        # Act
        dg_graph = DGGraph()
        output_node, current_idx = dg_graph._DGGraph__merge_consecutive_statement_nodes(
            nodes, node, idx
        )
        print(output_node)
        # Assert
        assert output_node.type.name == NodeType.STATEMENT.name
        assert output_node.info_type == "ASSIGN"
        assert output_node.indent == node.indent
        print(output_node.info.get("value"))
        print(expected_label)
        assert output_node.info.get("value") == expected_label
        assert current_idx == 4
