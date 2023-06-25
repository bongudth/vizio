from src.draw_graph.constants.shape import ShapeType
from src.draw_graph.services.node_transformers.base_dot_node import NodeTransformerBase


class RaiseNode(NodeTransformerBase):
    """
    Transform a conditional node to dotfile format
    """

    @property
    def label(self) -> str:
        return self.node.info.get("value")

    @property
    def shape(self):
        return ShapeType.ELLIPSE.value

    @property
    def color(self):
        return ""

    @property
    def fill_color(self) -> str:
        return "#F45050"

    @property
    def font_color(self) -> str:
        return "white"