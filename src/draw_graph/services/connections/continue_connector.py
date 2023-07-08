from typing import Any

from src.draw_graph.models.node_connection import NodeConnection
from src.draw_graph.services.connections.base_connector_handler import (
    BaseConnectionHandler,
)
from src.draw_graph.services.connections.condition_connector import ConditionConnector
from src.draw_graph.services.connections.loop_connector import LoopConnector


class ContinueConnector(BaseConnectionHandler):
    def handle_connections(self, **kwargs) -> tuple[Any, str]:
        nearest_parent_loop = LoopConnector.get_nearest_parent_loop_node(self.node)
        prev_node = self.node.prev_node
        if nearest_parent_loop and nearest_parent_loop.next_sibling:
            label = "continue"
            color = ConditionConnector.get_color(prev_node)
            appended_label = ConditionConnector.get_label(prev_node)
            label += f"/{appended_label}" if appended_label else ""
            self.connections = [
                NodeConnection(
                    prev_node,
                    nearest_parent_loop,
                    source="@continue_to_loop",
                    label=label,
                    color=color,
                    fontcolor=color,
                )
            ]
        return self.connections, self.text
