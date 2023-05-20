from typing import Any, Dict

from src.draw_graph.constants.node_types import NodeType
from src.draw_graph.models.dg_node import DGNode
from src.draw_graph.models.node_connection import NodeConnection
from src.draw_graph.models.same_rank import SameRank


class ReturnConnection:
    @classmethod
    def handle(cls, node: DGNode, end_node: DGNode) -> Dict[str, Any]:
        text = ""
        connections = []
        if node.next_node.type != NodeType.END:
            connections = [NodeConnection(node, end_node, source="@return_to_end")]
        if node.prev_node == node.parent:
            label = "True" if node.prev_node.type == NodeType.CONDITIONS else ""
            connections += [
                NodeConnection(node.prev_node, node, label=label, source="@return_2")
            ]
        if node.next_node.type != NodeType.END:
            text = f"{SameRank([node.prev_node, node]).to_dot()}"
        return {"text": text, "connections": connections}
