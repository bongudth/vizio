from typing import Any

from src.draw_graph.models.node_connection import NodeConnection
from src.draw_graph.services.connections.base_connection_handler import (
    BaseConnectionHandler,
)


class LoopConnection(BaseConnectionHandler):
    def handle(self) -> tuple[Any, Any]:
        if self.node.prev_node:
            connection = NodeConnection(
                self.node.prev_node, self.node, source="@prev_to_loop"
            )
            self._connections.append(connection)

        if self.node.next_sibling:
            connection = NodeConnection(
                self.node,
                self.node.next_sibling,
                label="out",
                source="@loop_to_next",
                color="red",
            )
            self._connections.append(connection)

        return self._connections, self._text
