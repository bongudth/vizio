from typing import Any, Dict, List, Union

from src.draw_graph.constants.node_types import NodeType
from src.draw_graph.models.dg_node import DGNode
from src.draw_graph.models.node_connection import NodeConnection
from src.draw_graph.services.connections.condition_connection import ConditionConnector
from src.draw_graph.services.connections.def_connection import DefConnector
from src.draw_graph.services.connections.loop_connection import LoopConnection
from src.draw_graph.services.connections.return_connection import ReturnConnection


class NodeConnectionsHandler:
    def __init__(self, nodes: List[DGNode]):
        self.nodes = []
        self.connections = []
        self.tree = None
        filtered_nodes = list(filter(lambda node: node.type != NodeType.COMMENT, nodes))
        self.nodes = filtered_nodes

    def parse_relationship_tree(self):
        for i, node in enumerate(self.nodes):
            if i > 0:
                node.prev_node = self.nodes[i - 1]
            if i + 1 < len(self.nodes):
                node.next_node = self.nodes[i + 1]

        for node in self.nodes:
            parent_node = self._get_parent_node(node)
            node.set_parent(parent_node)

        for i, node in enumerate(self.nodes):
            node.next_sibling = DGNode.get_next_sibling(node)

        for i, node in enumerate(self.nodes):
            node.prev_sibling = DGNode.get_prev_sibling(node)

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
        def_indent = -1
        len(self.nodes)
        node = None
        i = 0
        while node != self.nodes[-1]:
            node = self.nodes[i]
            text = ""
            connections = None
            response = None
            out_def_method = node.indent <= def_indent
            if out_def_method:
                def_indent = -1
                text += "}"
            elif NodeType.is_definition(node):
                def_indent = node.indent
                handler = DefConnector(node)
                _, text = handler.handle()
            elif NodeType.is_loop(node):
                handler = LoopConnection(node)
                connections, _ = handler.handle()
            elif NodeType.is_end(node):
                connections = [
                    NodeConnection(node.prev_node, node, source="@prev_to_end")
                ]
            elif NodeType.is_condition(node):
                handler = ConditionConnector(node)
                connections, _ = handler.handle()
            elif node.prev_node and node.prev_node.indent == node.indent:
                connections = [
                    NodeConnection(
                        node.prev_node, node, source="@prev_to_current_same_indent"
                    )
                ]
            elif NodeType.is_return(node):
                response = ReturnConnection.handle(node=node, end_node=self.nodes[-1])
                connections = response.get("connections", [])
            elif node.parent and self.nodes[i - 1] == node.parent:
                connections = [
                    NodeConnection(
                        node.parent,
                        node,
                        label="True",
                        source="@parent_to_child",
                        color="green",
                    )
                ]
            result += text or ""
            result += self._extract_text_from_connections(connections, response)
            if connections:
                node_connections.extend(connections)
            i += 1
        if def_indent != -1:
            result += "}\n"
        return dict(text=result, node_connections=node_connections)

    def _extract_text_from_connections(self, connections, response=None):
        text = response["text"] + "\n" if response else ""
        if not connections:
            return ""
        text += "\n".join([connection.to_dot() for connection in connections])
        return text + "\n"
