from typing import Any, Dict, List, Optional, Tuple

from src.analysis_code.constants.types import StatementType
from src.analysis_code.models.ac_node import ACNode
from src.draw_graph.constants.node_types import NodeType
from src.draw_graph.models.dg_node import DGNode
from src.draw_graph.services.graph_reporter import GraphReporter
from src.draw_graph.services.node_connections import NodeConnectionsHandler


class DGGraph:
    def __init__(self, lines: Optional[str] = None):
        self._lines = lines
        if self._lines:
            self._graph_reporter = GraphReporter()
            self._nodes = self.__parse_nodes()
            self._dg_nodes = self.__create_dg_nodes(self._nodes)
            self._node_connections = NodeConnectionsHandler(self._dg_nodes)
            self._node_connections.parse_relationship_tree()

    def __create_dg_nodes(self, nodes: List[ACNode]) -> List[DGNode]:
        full_nodes = [DGNode().to_diagram_type(NodeType.START)]
        # full_nodes.extend([DGNode(node) for node in nodes])
        node_index = 0
        while nodes and node_index < len(nodes):
            node = nodes[node_index]
            append_node = DGNode(node)
            if node.type == NodeType.STATEMENT.name:
                append_node, node_index = self.__merge_consecutive_statement_nodes(
                    nodes, node, node_index
                )

            if node.type in {
                NodeType.COMMENT.name,
                NodeType.UNKNOWN.name,
                NodeType.IGNORE.name,
            }:
                node_index += 1
                continue

            full_nodes.append(append_node)
            node_index += 1
        full_nodes.append(DGNode().to_diagram_type(NodeType.END))

        return full_nodes

    def __merge_consecutive_statement_nodes(
        self, nodes: List[ACNode], node: ACNode, idx: int
    ) -> Tuple[DGNode, int]:
        label = ""
        accepted_types = {NodeType.STATEMENT.name, NodeType.COMMENT.name}
        current_idx = idx
        while current_idx < len(nodes):
            p_node: DGNode = nodes[current_idx]
            if p_node.type == "COMMENT":
                current_idx += 1
                continue

            if p_node.type not in accepted_types or p_node.indent != node.indent:
                current_idx -= 1
                break

            current_idx += 1
            if p_node.info.get("value"):
                label += p_node.info.get("value") + "\n"

        ac_node = ACNode().from_dict(
            {
                "type": NodeType.STATEMENT.name,
                "info": {"type": StatementType.ASSIGN.name, "value": label},
                "indent": node.indent,
                "line_no": node.line_no,
            }
        )
        output_node = DGNode(ac_node)
        return output_node, current_idx

    def __parse_nodes(self) -> List[ACNode]:
        nodes = []
        for line in self._lines:
            if isinstance(line, str):
                formatted_line = line.rstrip()
                node = ACNode().from_string(formatted_line)
            else:
                print("line", line)
                node = ACNode().from_dict(line)
            nodes.append(node)
        return nodes

    def build_node_connections(self) -> Dict[str, Any]:
        result = self.node_connections.render()
        self._node_connections = result.get("node_connections")
        return result

    @property
    def dg_nodes(self) -> List[DGNode]:
        return self._dg_nodes

    @property
    def node_connections(self) -> NodeConnectionsHandler:
        return self._node_connections

    @property
    def report(self):
        return self._graph_reporter.get_report(self)
