from ast import literal_eval
from typing import Any, Dict, Optional, Union

from src.analysis_code.constants.types import ConditionType, StatementType
from src.analysis_code.models.ac_node import ACNode
from src.draw_graph.constants.node_types import NodeType

IGNORE_TYPES = [NodeType.DEF, NodeType.COMMENT]
IGNORE_INFO_TYPES = [
    ConditionType.ELSE.name,
    StatementType.BREAK.name,
    StatementType.CONTINUE.name,
]


class DGNode:
    def __init__(self, data: Union[ACNode, None] = None):
        self.id = f"L{data.line_no}" if data else id(self)
        self.data = data or {}
        self.diagram_type = None
        self._prev_sibling = None
        self._next_sibling = None
        self._prev_node = None
        self._next_node = None
        self.parent = None

    def set_id(self, id: int):
        self.id = f"L{id}"

    def set_parent(self, parent=None):
        self.parent = parent

    def set_next_sibling(self, node: "DGNode"):
        self.next_sibling = node

    def set_prev_sibling(self, node: "DGNode"):
        self.prev_sibling = node

    def to_diagram_type(self, node_type: NodeType):
        self.diagram_type = node_type
        return self

    @property
    def type(self) -> NodeType:
        node_type_text = getattr(self.data, "type", "")
        return NodeType[node_type_text] if node_type_text else self.diagram_type

    @property
    def info(self) -> Dict[str, Any]:
        return self.data.info

    @property
    def info_type(self) -> str:
        return self.data.info_type if self.data else ""

    @property
    def indent(self) -> int:
        return getattr(self.data, "indent", 0)

    @property
    def line_no(self) -> int:
        return self.data.line_no if self.data else 0

    @property
    def is_hidden(self) -> bool:
        return any(
            [
                self.type in IGNORE_TYPES,
                self.info_type in IGNORE_INFO_TYPES,
                self.is_hidden_node,
            ]
        )

    def from_string(self, string: str) -> "DGNode":
        self.data = literal_eval(string)
        return self

    @property
    def prev_sibling(self):
        return self._prev_sibling

    @prev_sibling.setter
    def prev_sibling(self, value):
        self._prev_sibling = value

    @property
    def next_sibling(self):
        return self._next_sibling

    @next_sibling.setter
    def next_sibling(self, value):
        self._next_sibling = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        self._next_node = value

    @property
    def prev_node(self):
        return self._prev_node

    @prev_node.setter
    def prev_node(self, value: "DGNode" = None):
        self._prev_node = value

    def __repr__(self):
        return f"NODE: {self.data}"

    @classmethod
    def get_prev_sibling(cls, node: "DGNode") -> Optional["DGNode"]:
        indent = node.indent
        while node.prev_node:
            if node.prev_node.indent == indent:
                return node.prev_node
            if node.prev_node.indent < indent:
                return None
            node = node.prev_node

    @classmethod
    def get_next_sibling(cls, node: "DGNode") -> Optional["DGNode"]:
        indent = node.indent
        while node.next_node:
            if (
                not NodeType.is_start(node.next_node)
                and node.next_node.indent == indent
            ):
                return node.next_node
            if node.next_node.indent < indent:
                return None
            node = node.next_node

    @property
    def last_child(self) -> Optional["DGNode"]:
        if not self.is_empty(self.next_sibling):
            return self.next_sibling.prev_node

        p_node = self
        while p_node.is_empty(p_node.next_node):
            p_node = p_node.next_node

        return p_node

    @classmethod
    def is_empty(cls, node) -> bool:
        return not node or not node.data

    @property
    def is_hidden_node(self) -> bool:
        if self.type == NodeType.RETURN:
            return not self.info
        return False

    def get_first_child(self):
        first_node = self.next_node
        if first_node and first_node.indent > self.indent:
            return first_node
        return None

    def get_last_child(self):
        first_node = self.next_node
        p_node = first_node
        while p_node.next_sibling:
            if not p_node.next_sibling:
                return p_node
            p_node = p_node.next_sibling
        return p_node

    def has_child(self):
        return self.next_node and self.next_node.indent > self.indent

    def get_last_descendant(self):
        if not self.has_child():
            return None

        p_node = self
        while p_node.has_child():
            p_node = p_node.get_last_child()
        return p_node
