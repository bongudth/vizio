from typing import Any, Dict, List, Union

from logger.app_log import AppLog
from src.draw_graph.constants.node_types import NodeType
from src.draw_graph.models.dg_node import DGNode
from src.draw_graph.models.node_connection import NodeConnection
from src.draw_graph.services.connections.condition_connector import ConditionConnector
from src.draw_graph.services.connections.def_connector import DefConnector
from src.draw_graph.services.connections.loop_connector import LoopConnector
from src.draw_graph.services.connections.return_connector import ReturnConnector


class NodeConnectionsHandler:
    def __init__(self, nodes: List[DGNode]):
        self.nodes = []
        self.connections = []
        self.tree = None
        filtered_nodes = list(filter(lambda node: node.type != NodeType.COMMENT, nodes))
        self.nodes = filtered_nodes

    def parse_relationship_tree(self):
        for i, node in enumerate(self.nodes):
            node.prev_node = self.nodes[i - 1] if i > 0 else None
            node.next_node = self.nodes[i + 1] if i + 1 < len(self.nodes) else None

        [node.set_parent(self._get_parent_node(node)) for node in self.nodes]
        [node.set_next_sibling(DGNode.get_next_sibling(node)) for node in self.nodes]
        [node.set_prev_sibling(DGNode.get_prev_sibling(node)) for node in self.nodes]

    def _get_parent_node(self, node: DGNode) -> Union[DGNode, None]:
        parent_node = node.prev_node
        if not parent_node:
            return None
        while node.indent <= parent_node.indent:
            parent_node = parent_node.prev_node
            if not parent_node:
                break
        return parent_node

    def render(self) -> Dict[str, Any]:
        result = ""
        node_connections = []
        self.nodes[0]
        end_node = self.nodes[-1]
        node = None
        i = 0
        out_def_node = None
        while node != self.nodes[-1]:
            node = self.nodes[i]
            text = ""
            connections = []
            if node == out_def_node:
                text += "}\n"
                out_def_node = None

            if NodeType.is_definition(node):
                handler = DefConnector(node)
                _connections, _text = handler.handle()
                out_def_node = handler.get_out_def_node(end_node=end_node)
                text += f"\n{_text}"
                connections.extend(_connections)
            elif NodeType.is_loop(node):
                handler = LoopConnector(node)
                _connections, _ = handler.handle()
                connections.extend(_connections)
                handler.get_last_child()
            elif NodeType.is_condition(node):
                handler = ConditionConnector(node)
                connections, _ = handler.handle()
            elif NodeType.is_return(node):
                handler = ReturnConnector(node)
                connections, text = handler.handle(end_node=end_node)
            elif (
                node.next_node
                and node.next_node.prev_sibling
                and NodeType.is_loop(node.next_node.prev_sibling)
            ):
                connections = []
            elif node.next_node and not any(
                [
                    NodeType.is_condition_elif(node.next_node),
                    NodeType.is_end(node.next_node),
                ]
            ):
                connections = [
                    NodeConnection(node, node.next_node, source="@current_to_next")
                ]
            result += text or ""
            result += self._extract_text_from_connections(connections)

            if connections:
                node_connections.extend(connections)
            i += 1

        if out_def_node:
            result += "}\n"

        return dict(text=result, node_connections=node_connections)

    def _extract_text_from_connections(self, connections: List[NodeConnection]):
        return "\n".join([connection.to_dot() for connection in connections]) + "\n"
