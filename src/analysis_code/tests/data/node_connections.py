"""
Module for building node connections
It takes a list of nodes and returns a string of dot code.
"""
from typing import Any, Dict, List, Union

from src.draw_graph.constants.node_types import NodeType
from src.draw_graph.models.dg_node import DGNode
from src.draw_graph.models.node_connection import NodeConnection
from src.draw_graph.services.connections.condition_connection import ConditionConnector
from src.draw_graph.services.connections.def_connection import DefConnector
from src.draw_graph.services.connections.loop_connection import LoopConnection
from src.draw_graph.services.connections.return_connection import ReturnConnection


# It takes a list of nodes, and returns a string of dot code
class NodeConnections:
    nodes: List[DGNode] = []
    connections: List[NodeConnection] = []
    tree = None

    def __init__(self, nodes: List[DGNode]):
        filtered_nodes = list(filter(lambda node: node.type != NodeType.COMMENT, nodes))
        self.__class__.nodes = filtered_nodes

    @classmethod
    def parse_relationship_tree(cls):
        """
        For each node, set the previous node, next node, parent node, and anode

        :param cls: the class that the method is being called from
        """
        for i in range(len(cls.nodes)):
            if i > 0:
                cls.nodes[i].prev_node = cls.nodes[i - 1]
            if i + 1 < len(cls.nodes):
                cls.nodes[i].next_node = cls.nodes[i + 1]

        for node in cls.nodes:
            parent_node = cls._get_parent_node(node)
            node.set_parent(parent_node)

        for i in range(len(cls.nodes)):
            cls.nodes[i].next_sibling = DGNode.get_next_sibling(cls.nodes[i])

        for i in range(len(cls.nodes)):
            cls.nodes[i].prev_sibling = DGNode.get_prev_sibling(cls.nodes[i])

    @classmethod
    def _get_parent_node(cls, node: DGNode) -> Union[DGNode, None]:
        """
        > Get the parent node of a node by going back to the previous node and checking if the
        indentation is less than the current node's indentation

        :param cls: The class that the method is being called on
        :param node: The node to get the parent of
        :type node: Node
        :return: The parent node of the node passed in.
        """
        parent_node = node.prev_node
        if not parent_node:
            return None
        while node.indent <= parent_node.indent:
            parent_node = parent_node.prev_node
            if not parent_node:
                break
        return parent_node

    @classmethod
    def render(cls) -> Dict[str, Any]:
        """
        It takes a list of nodes and returns a string of dot code

        :param cls: The class that the method is being called on
        :return: The result of the render method.
        """
        result = ""
        node_connections = []
        def_indent = -1
        for i, node in enumerate(cls.nodes):
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
                response = ReturnConnection.handle(node=node, end_node=cls.nodes[-1])
                connections = response.get("connections", [])

            elif node.parent and cls.nodes[i - 1] == node.parent:
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
            result += cls.extract_text_from_connections(connections, response)
            if connections:
                node_connections.extend(connections)
        if def_indent != -1:
            result += "}"
        return dict(text=result, node_connections=node_connections)

    @classmethod
    def extract_text_from_connections(cls, connections, response=None):
        text = response["text"] + "\n" if response else ""
        if not connections:
            return ""
        text += "\n".join([connection.to_dot() for connection in connections])
        return text
