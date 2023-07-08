from typing import List

from src.draw_graph.services.dg_graph import DGGraph
from src.draw_graph.services.node_transform_handler import NodeTransformerHandler


class DotfileBodyCreator:
    def __init__(self, lines: List[str], background_color="white", **kwargs):
        self.list_summary = kwargs.get("list_summary")
        self.node_transformers_handler = NodeTransformerHandler(
            list_summary=self.list_summary
        )
        self.lines = lines
        self.background_color = background_color
        self.dg_graph = DGGraph(lines)

    def create(self) -> str:
        return f'bgcolor="{self.background_color}"\nnode [fontname="courier"]\n{self._build_nodes()}{self._build_node_connections()}'

    def _build_nodes(self) -> str:
        result = ""
        for node in self.dg_graph.dg_nodes:
            transformed_node = self.node_transformers_handler.transform(node)
            if transformed_node:
                content = transformed_node.get("content", "")
                result += content
        return result

    def _build_node_connections(self) -> str:
        result = self.dg_graph.build_node_connections()
        return result.get("text")

    def get_report(self):
        return self.dg_graph.report
