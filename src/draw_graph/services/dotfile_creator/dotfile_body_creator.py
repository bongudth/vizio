from typing import List

from src.draw_graph.services.dg_graph import DGGraph
from src.draw_graph.services.node_transform_handler import NodeTransformerHandler


class DotfileBodyCreator:
    node_transformers_handler = NodeTransformerHandler()

    def __init__(self, lines: List[str], background_color="white"):
        self.lines = lines
        self.background_color = background_color
        self.dg_graph = DGGraph(lines)

    def create(self) -> str:
        return f'bgcolor="{self.background_color}"\n{self._build_nodes()}{self._build_node_connections()}'

    def _build_nodes(self) -> str:
        return "".join(
            transformed_node.get("content", "")
            for node in self.dg_graph.get_dg_nodes()
            if (transformed_node := self.node_transformers_handler.transform(node))
        )

    def _build_node_connections(self) -> str:
        result = self.dg_graph.build_node_connections()
        return result.get("text")

    def get_report(self):
        return self.dg_graph.get_report()
