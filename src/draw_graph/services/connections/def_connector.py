from typing import Any, Optional

from src.draw_graph.models.dg_node import DGNode
from src.draw_graph.models.node_connection import NodeConnection, SimpleNodeConnection
from src.draw_graph.services.connections.base_connector_handler import (
    BaseConnectionHandler,
)


class DefConnector(BaseConnectionHandler):
    def handle_connections(self) -> tuple[Any, str]:
        text = f'subgraph cluster_{self.node.info["name"]} {{\n'
        text += f'label = "{self.node.info["value"]}";\n'

        self._connections = []
        return self._connections, text

    def get_out_def_node(self, end_node: DGNode) -> Optional[DGNode]:
        return (
            end_node
            if DGNode.is_empty(self.node.next_sibling)
            else self.node.next_sibling
        )
