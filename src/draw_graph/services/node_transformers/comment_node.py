from src.draw_graph.services.node_transformers.base_dot_node import NodeTransformerBase


class CommentNode(NodeTransformerBase):
    """
    Transform a conditional node to dotfile format
    """

    @property
    def is_hidden(self) -> bool:
        return True
