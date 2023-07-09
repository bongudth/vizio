from typing import Any

from src.draw_graph.constants.node_types import NodeType
from src.draw_graph.models.node_connection import NodeConnection
from src.draw_graph.services.connections.base_connector_handler import (
    BaseConnectionHandler,
)
from src.draw_graph.services.connections.loop_connector import LoopConnector


class BreakConnector(BaseConnectionHandler):
    def handle_connections(self, **kwargs) -> tuple[Any, str]:
        end_node = kwargs.get("end_node")
        nearest_parent_loop = LoopConnector.get_nearest_parent_loop_node(self.node)
        prev_node = self.node.prev_node
        if nearest_parent_loop:
            if not nearest_parent_loop.next_sibling:
                label = "break"
                color = "red"
                fontcolor = "red"
                if NodeType.is_condition_if(prev_node) or NodeType.is_condition_elif(
                    prev_node
                ):
                    label = "true -> break"
                    color = "green"
                    fontcolor = "green"
                elif NodeType.is_condition_else(prev_node):
                    label = "false -> break"
                    color = "red"
                    fontcolor = "red"

                self.connections = [
                    NodeConnection(
                        prev_node,
                        end_node,
                        source="@break_to_end_node",
                        label=label,
                        color=color,
                        fontcolor=fontcolor,
                    )
                ]
            else:
                self.connections = [
                    NodeConnection(
                        prev_node,
                        nearest_parent_loop.next_sibling,
                        source="@break_to_next_sibling_of_loop",
                        label="break",
                        color="red",
                        fontcolor="red",
                    )
                ]
        return self.connections, self.text
