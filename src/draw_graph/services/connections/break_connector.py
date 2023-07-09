from typing import Any

from src.draw_graph.constants.node_types import NodeType
from src.draw_graph.models.dg_node import DGNode
from src.draw_graph.models.node_connection import NodeConnection
from src.draw_graph.services.connections.base_connector_handler import (
    BaseConnectionHandler,
)
from src.draw_graph.services.connections.loop_connector import LoopConnector


class BreakConnector(BaseConnectionHandler):
    def handle_connections(self, **kwargs) -> tuple[Any, str]:
        end_node = kwargs.get("end_node")
        nearest_parent_loop = LoopConnector.get_nearest_parent_loop_node(self.node)
        self.connections += self.handle_nearest_parent_loop(
            end_node, nearest_parent_loop
        )
        return self.connections, self.text

    def handle_nearest_parent_loop(
        self, end_node: DGNode, nearest_parent_loop: DGNode
    ) -> list[NodeConnection]:
        connections = []
        prev_node = self.node.parent
        if nearest_parent_loop:
            if not nearest_parent_loop.next_sibling or NodeType.is_return(
                nearest_parent_loop.next_sibling
            ):
                label = "break"
                color = "red"
                fontcolor = "red"
                if NodeType.is_condition_if(prev_node) or NodeType.is_condition_elif(
                    prev_node
                ):
                    label = "true -> break"
                    color = "green"
                    fontcolor = "green"
                    src_node = prev_node
                elif NodeType.is_condition_else(prev_node):
                    label = "false -> break"
                    color = "red"
                    fontcolor = "red"
                    src_node = prev_node.prev_sibling

                connections.append(
                    NodeConnection(
                        src_node,
                        end_node,
                        source="@break_to_end_node",
                        label=label,
                        color=color,
                        fontcolor=fontcolor,
                    )
                )
            else:
                connections.append(
                    NodeConnection(
                        prev_node,
                        nearest_parent_loop.next_sibling,
                        source="@break_to_next_sibling_of_loop",
                        label="break",
                        color="red",
                        fontcolor="red",
                    )
                )
        return connections
