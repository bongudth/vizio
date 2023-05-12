from typing import Any

from src.draw_graph.services.connections.base_connection_handler import (
    BaseConnectionHandler,
)


class DefConnector(BaseConnectionHandler):
    def handle(self) -> tuple[Any, str]:
        text = f'subgraph cluster_{self.node.info["name"]} {{\n'
        text += f'label = "{self.node.info["name"]}";\n'
        return None, text
