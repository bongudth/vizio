from typing import Any

from src.draw_graph.constants.node_types import NodeType
from src.draw_graph.models.dg_node import DGNode
from src.draw_graph.models.node_connection import NodeConnection
from src.draw_graph.services.connections.base_connector_handler import (
    BaseConnectionHandler,
)


class LoopConnector(BaseConnectionHandler):
    def handle_connections(self, **kwargs) -> tuple[Any, Any]:
        end_node = kwargs.get("end_node")
        self._connections = [
            self.connect_loop_to_next(),
            self.connect_loop_to_next_sibling(),
            self.connect_loop_to_parent_loop(),
            self.connect_last_node_to_loop(),
            self.connect_end_loop_to_end(end_node),
        ]
        self._text = ""
        self._connections = list(filter(lambda x: x is not None, self._connections))
        return self._connections, self._text

    def connect_loop_to_next(self) -> NodeConnection:
        connection = None
        if self.node.next_node:
            connection = NodeConnection(
                self.node, self.node.next_node, source="@loop_to_next"
            )
        return connection

    def connect_loop_to_next_sibling(self) -> NodeConnection:
        connection = None
        if self.node.next_sibling:
            connection = NodeConnection(
                self.node,
                self.node.next_sibling,
                label="out",
                source="@loop_to_next_sibling",
                color="red",
            )
            self._connections.append(connection)
        return connection

    def connect_loop_to_parent_loop(self) -> NodeConnection:
        connection = None
        if (
            not self.node.next_sibling
            and self.node.parent
            and NodeType.is_loop(self.node.parent)
        ):
            connection = NodeConnection(
                self.node,
                self.node.parent,
                label="out",
                source="@loop_to_parent_loop",
                color="red",
            )
            self._connections.append(connection)
        return connection

    def connect_last_node_to_loop(self) -> NodeConnection:
        last_node = self.node.get_last_child()

        if NodeType.is_loop(last_node):
            return None

        return NodeConnection(
            last_node,
            self.node,
            source="@last_to_loop",
            color="blue",
        )

    def connect_end_loop_to_end(self, end_node) -> NodeConnection:
        if (
            not self.node.next_sibling
            and NodeType.is_loop(self.node)
            and NodeType.is_start(self.node.parent)
        ):
            return NodeConnection(
                self.node,
                end_node,
                source="@end_loop_to_end",
                color="red",
                label="out",
            )