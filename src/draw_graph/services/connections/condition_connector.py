from typing import List, Optional

from src.analysis_code.constants.types import ConditionType
from src.draw_graph.constants.node_types import NodeType
from src.draw_graph.models.dg_node import DGNode
from src.draw_graph.models.node_connection import NodeConnection
from src.draw_graph.models.same_rank import SameRank
from src.draw_graph.services.connections.base_connector_handler import (
    BaseConnectionHandler,
)


class ConditionConnector(BaseConnectionHandler):
    def handle_connections(self, **kwargs):
        end_node = kwargs.get("end_node")
        self._connections = self.connect_nodes_based_on_conditions(self.node)
        self._connections = self.merge_if_elif_to_next_statement(
            self._connections, self.node, end_node=end_node
        )
        self._text = self._handle_same_rank()
        return self._connections, self._text

    @classmethod
    def connect_nodes_based_on_conditions(
        cls, node: "DGNode"
    ) -> Optional[List[NodeConnection]]:
        """
        :param node: Condition node

        * A A' => Z -> A
        * B B' => A -> B
        * C C' => C -> C'
        :return: connection, if_node_stack
        """
        connections = []
        info_type: str = node.info_type
        if info_type == ConditionType.IF.name:
            connections = cls._connect_if_nodes(node)
        elif info_type == ConditionType.ELIF.name:
            connections = cls._connect_elif_nodes(node)
        elif info_type == ConditionType.ELSE.name:
            connections = cls._connect_else_nodes(node)
        return connections

    @classmethod
    def get_color(cls, node: "DGNode") -> str:
        if NodeType.is_condition_if(node) or NodeType.is_condition_elif(node):
            return "green"
        if NodeType.is_condition_else(node):
            return "red"
        return ""

    @classmethod
    def get_label(cls, node: "DGNode") -> str:
        if NodeType.is_condition_if(node) or NodeType.is_condition_elif(node):
            return "true"
        if NodeType.is_condition_else(node):
            return "false"
        return ""

    @classmethod
    def _connect_if_nodes(cls, node: "DGNode") -> List[NodeConnection]:
        connections = []
        connections += cls._connect_if_prev_sibling_nodes(node)
        connections += cls._connect_if_next_nodes(node)
        connections += cls._connect_if_elif_nodes(node)
        connections += cls._connect_out_scope_node(node)
        return connections

    @classmethod
    def _connect_elif_nodes(cls, node: "DGNode") -> List[NodeConnection]:
        connections = []
        connections += cls._connect_if_next_nodes(node)
        return connections

    @classmethod
    def _connect_if_prev_sibling_nodes(cls, node: "DGNode") -> List[NodeConnection]:
        connections = []
        if (
            not DGNode.is_empty(node.prev_sibling)
            and node.prev_sibling.type == NodeType.CONDITIONS
        ):
            connections = [
                NodeConnection(
                    node.prev_sibling,
                    node,
                    label="false",
                    source="@if_to_prev_sibling",
                    color="red",
                    fontcolor="red",
                )
            ]
        return connections

    @classmethod
    def _connect_if_prev_nodes(cls, node: "DGNode") -> List[NodeConnection]:
        connections = []
        if not (
            not DGNode.is_empty(node.prev_sibling)
            and (
                node.prev_sibling.type == NodeType.LOOP
                or node.prev_node.type in [NodeType.RETURN]
            )
        ):
            connections = [
                NodeConnection(node.prev_node, node, source="@if_to_prev_node")
            ]
        return connections

    @classmethod
    def _connect_if_next_nodes(cls, node: "DGNode") -> List[NodeConnection]:
        connections = []
        if node.next_node:
            connections = [
                NodeConnection(
                    node,
                    node.next_node,
                    label="true",
                    color="green",
                    source="@if_to_next_node",
                    fontcolor="green",
                )
            ]
        return connections

    @classmethod
    def _connect_if_elif_nodes(cls, node: "DGNode") -> List[NodeConnection]:
        connections = []
        p_node = node
        while (
            p_node.next_sibling
            and p_node.next_sibling.info_type == ConditionType.ELIF.name
        ):
            connections.append(
                NodeConnection(
                    p_node,
                    p_node.next_sibling,
                    label="false",
                    color="red",
                    source="@if_or_if_to_elif",
                    fontcolor="red",
                )
            )
            p_node = p_node.next_sibling
        return connections

    @classmethod
    def _connect_else_nodes(cls, node: "DGNode") -> List[NodeConnection]:
        return [
            NodeConnection(
                node.prev_sibling,
                node.next_node,
                label="false",
                color="red",
                source="@elif_to_else",
                fontcolor="red",
            )
        ]

    @classmethod
    def _connect_out_scope_node(cls, node: "DGNode") -> List[NodeConnection]:
        connections = []
        p_node = node
        out_scope_node = cls._get_out_condition_scope_node(p_node)
        if (
            not DGNode.is_empty(p_node.next_sibling)
            and p_node.next_sibling.type != NodeType.CONDITIONS
            and out_scope_node.indent == p_node.indent
        ):
            connections.append(
                NodeConnection(
                    node,
                    out_scope_node,
                    label="false",
                    source="@if_to_next_sibling",
                    color="red",
                    fontcolor="red",
                )
            )
        return connections

    @classmethod
    def merge_if_elif_to_next_statement(
        cls, connections: List[NodeConnection], node: DGNode, **kwargs
    ) -> List[NodeConnection]:
        out_scope_node = cls._get_out_condition_scope_node(node)
        last_child = node.get_last_child()
        end_node = kwargs.get("end_node")
        if (
            NodeType.is_condition(node)
            and not NodeType.is_return(last_child)
            and not NodeType.is_raise(last_child)
            and last_child != out_scope_node
            and not NodeType.is_return(last_child.get_last_child())
        ):
            if out_scope_node:
                connections.append(
                    NodeConnection(
                        last_child,
                        out_scope_node,
                        source="@last_child_to_next_sibling",
                    )
                )
            elif not last_child.next_node:
                connections.append(
                    NodeConnection(
                        last_child,
                        end_node,
                        source="@if_last_child_to_end_node",
                    )
                )
        if (
            node.info_type in [ConditionType.IF.name]
            and last_child.info_type in [ConditionType.IF.name]
            and NodeType.is_return(last_child.get_last_child())
        ):
            connections.append(
                NodeConnection(
                    last_child,
                    out_scope_node,
                    source="@if_last_child_to_next_sibling",
                    label="false",
                    color="red",
                    fontcolor="red",
                )
            )
        return connections

    def _handle_same_rank(self):
        if NodeType.is_return(self.node.next_node):
            return SameRank(
                [self.node, self.node.next_node], source="@condition_and_return"
            ).to_dot()
        return ""

    @classmethod
    def _get_else_node(cls, node: DGNode):
        else_node = None
        p_node = node.next_sibling
        while (
            p_node.type == NodeType.COMMENT
            or p_node.info_type == ConditionType.ELIF.name
        ):
            p_node = p_node.next_sibling
        if (
            p_node.type == NodeType.CONDITIONS
            and p_node.info_type == ConditionType.ELSE.name
        ):
            else_node: DGNode = p_node
        return else_node

    @classmethod
    def _get_out_condition_scope_node(cls, node: DGNode) -> DGNode:
        temp_node = node.next_sibling
        while temp_node and temp_node.type == NodeType.CONDITIONS:
            temp_node = temp_node.next_sibling

        if temp_node and temp_node.indent == node.indent:
            return temp_node

        return None
