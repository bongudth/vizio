from typing import Any, Dict, List

from src.analysis_code.models.ac_node import ACNode
from src.draw_graph.constants.node_types import NodeType
from src.draw_graph.models.dg_node import DGNode
from src.draw_graph.services.graph_reporter import GraphReporter
from src.draw_graph.services.node_connections import NodeConnections


class DGGraph:
    def __init__(self, lines):
        self._lines = lines
        self._graph_reporter = GraphReporter()
        self._nodes = None
        self._dg_nodes = None
        self._node_connections = None
        self.__create_tree()

    def __create_tree(self):
        self._nodes = self.__parse_nodes()
        self._dg_nodes = self.__create_dg_nodes(self._nodes)
        node_connections = NodeConnections(self._dg_nodes)
        node_connections.parse_relationship_tree()
        self._node_connections = node_connections

    def __create_dg_nodes(self, nodes: List[ACNode]) -> List[DGNode]:
        full_nodes = [DGNode().to_diagram_type(NodeType.START)]
        full_nodes.extend([DGNode(node) for node in nodes])
        full_nodes.append(DGNode().to_diagram_type(NodeType.END))
        return full_nodes

    def __parse_nodes(self) -> List[ACNode]:
        nodes = []
        for line in self._lines:
            if isinstance(line, str):
                formatted_line = line.rstrip()
                node = ACNode().from_string(formatted_line)
            else:
                node = ACNode().from_dict(line)
            nodes.append(node)
        return nodes

    def build_node_connections(self) -> Dict[str, Any]:
        result = NodeConnections.render()
        self._node_connections = result.get("node_connections")
        return result

    @property
    def dg_nodes(self) -> List[DGNode]:
        return self._dg_nodes

    @property
    def node_connections(self) -> NodeConnections:
        return self._node_connections

    @property
    def report(self):
        return self._graph_reporter.get_report(self)
