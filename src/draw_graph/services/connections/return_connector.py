from typing import Any, Dict, List

from src.draw_graph.constants.node_types import NodeType
from src.draw_graph.models.dg_node import DGNode
from src.draw_graph.models.node_connection import NodeConnection
from src.draw_graph.services.connections.base_connector_handler import (
    BaseConnectionHandler,
)


class ReturnConnector(BaseConnectionHandler):
    def handle_connections(self, **kwargs) -> Dict[str, Any]:
        node = self.node
        end_node = kwargs.get("end_node")
        text = ""
        connections: List[NodeConnection] = []
        connections = [NodeConnection(node, end_node, source="@return_to_end")]

        if not node.info:
            if node.prev_node.type == NodeType.CONDITIONS:
                connections += [
                    NodeConnection(
                        node.prev_node,
                        end_node,
                        color="green",
                        label="true",
                        source="@if_node_to_return",
                        fontcolor="green",
                    )
                ]
        else:
            if node.prev_node == node.parent:
                label = "true" if node.prev_node.type == NodeType.CONDITIONS else ""
                # connections += [
                #     NodeConnection(
                #         node.prev_node,
                #         node,
                #         color="green",
                #         label=label,
                #         source="@return_to_prev",
                #     )
                # ]

        self.connections = connections
        self.text = text
        return self.connections, self.text
