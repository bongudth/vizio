from src.draw_graph.constants.shape import ShapeType
from src.draw_graph.services.node_transformers.base_dot_node import NodeTransformerBase


class DefaultNode(NodeTransformerBase):
    """
    Transform a conditional node to dotfile format
    """

    @property
    def label(self) -> str:
        return str(self.node.info)

    @property
    def shape(self):
        return ShapeType.RECTANGLE.value

    @property
    def color(self):
        return ""
