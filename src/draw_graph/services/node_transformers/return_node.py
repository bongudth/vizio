from src.draw_graph.constants.shape import ShapeType
from src.draw_graph.services.node_transformers.base_dot_node import NodeTransformerBase


class ReturnNode(NodeTransformerBase):
    """
    Transform a conditional node to dotfile format
    """

    @property
    def label(self) -> str:
        return self.node.info.get("name")

    @property
    def shape(self):
        return ShapeType.ELLIPSE.value

    @property
    def color(self):
        return ""

    @property
    def fill_color(self) -> str:
        return "#BAD7E9"

    @property
    def font_color(self) -> str:
        return "black"
