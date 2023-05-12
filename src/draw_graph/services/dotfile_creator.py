from typing import List

from src.draw_graph.models.dg_node import DGNode
from src.draw_graph.services.dg_node_graph import DGNodeGraph
from src.draw_graph.services.node_transform_handler import NodeTransformerHandler


class DotfileCreator:
    def __init__(self, lines):
        self._lines = lines
        self._node_transformers_handler = NodeTransformerHandler()
        self._node_structure = DGNodeGraph(lines)
        self._title = "my_graph"
        self._dot_file_content = ""
        self._background_color = "white"

    def generate(self):
        return self.__build_header() + self.__build_body() + "}"

    def __build_header(self):
        return f"digraph {self._title} {{\n"

    def __build_body(self):
        self.__build_node_connection_content()

        body = ""
        body += f'bgcolor="{self._background_color}"\n'
        body += self.__build_nodes_content(self._node_structure.get_dg_nodes())
        body += self._dot_file_content
        return body

    def __build_nodes_content(self, nodes: List[DGNode]):
        node_content = ""
        if not nodes:
            return node_content
        for node in nodes:
            response = self._node_transformers_handler.transform(node)
            node_content += response.get("content") or ""
        return node_content

    def __build_node_connection_content(self):
        result = self._node_structure.build_connections()
        self._dot_file_content = result.get("text")

    def get_report(self):
        return self._node_structure.get_report()
