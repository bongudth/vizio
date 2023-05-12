from typing import List

from src.draw_graph.models.dg_node import DGNode


class SameRank:
    def __init__(self, nodes: List[DGNode]):
        self._nodes = nodes

    def to_dot(self) -> str:
        node_ids = [str(node.id) for node in self._nodes if not node.is_hidden]
        text = "; ".join(list(node_ids))
        return f"{{rank = same; {text};}}"
