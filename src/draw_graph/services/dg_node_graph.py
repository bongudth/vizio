import traceback
from typing import Any, Dict, List

from src.analysis_code.models.ac_node import ACNode
from src.draw_graph.constants.node_types import NodeType
from src.draw_graph.models.dg_node import DGNode
from src.draw_graph.services.graph_reporter import GraphReporter
from src.draw_graph.services.node_connections import NodeConnections
from src.logger.app_log import AppLog


class DGNodeGraph:
    def __init__(self, lines):
        self._lines = lines
        self._graph_reporter = GraphReporter()
        self._nodes = None
        self._dg_nodes = None
        self._node_connections = None
        self.__create_tree()

    def __create_tree(self):
        try:
            self._nodes = self.__create_nodes()
            self._dg_nodes = self.__create_dg_nodes(self._nodes)
            NodeConnections(self._dg_nodes).parse_relationship_tree()
        except Exception as e:
            AppLog.error(e)
            AppLog.error(traceback.format_exc())

    def __create_dg_nodes(self, nodes: List[ACNode]) -> List[DGNode]:
        full_nodes = [DGNode().to_diagram_type(NodeType.START)]
        full_nodes.extend([DGNode(node) for node in nodes])
        full_nodes.append(DGNode().to_diagram_type(NodeType.END))
        return full_nodes

    def __create_nodes(self) -> List[ACNode]:
        nodes = []
        for idx in range(len(self._lines)):
            if isinstance(self._lines[idx], str):
                formatted_line = self._lines[idx].rstrip()
                node = ACNode().from_string(formatted_line)
            else:
                node = ACNode().from_dict(self._lines[idx])
            nodes.append(node)
        return nodes

    def build_connections(self) -> Dict[str, Any]:
        result = NodeConnections.render()
        self._node_connections = result.get("node_connections")
        return result

    def get_dg_nodes(self) -> List[DGNode]:
        return self._dg_nodes

    def get_node_connections(self) -> NodeConnections:
        return self._node_connections

    def get_report(self):
        return self._graph_reporter.get_report(self)
