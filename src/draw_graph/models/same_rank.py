from typing import List

from src.draw_graph.models.dg_node import DGNode


class SameRank:
    def __init__(self, nodes: List[DGNode]):
        self._nodes = nodes

    def to_dot(self) -> str:
        # sourcery skip: remove-unnecessary-cast
        node_ids = [str(node.id) for node in self._nodes if not node.is_hidden]
        if len(node_ids) < 2:
            return ""
        text = "; ".join(list(node_ids))
        return f"{{rank=same; {text};}}"
