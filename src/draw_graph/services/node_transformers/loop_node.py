from src.draw_graph.constants.shape import ShapeType
from src.draw_graph.services.node_transformers.base_dot_node import NodeTransformerBase


class LoopNode(NodeTransformerBase):
    """
    Transform a conditional node to dotfile format
    """

    @property
    def label(self) -> str:
        if self.node.info.get("type") == "FOR":
            return f"Loop {self.node.info.get('item')} in {self.node.info.get('list')}"
        return f"While {self.node.info.get('conditions')}"

    @property
    def shape(self):
        return ShapeType.RECTANGLE.value

    @property
    def color(self):
        return ""

    @property
    def fill_color(self) -> str:
        return "#6D67E4"

    @property
    def font_color(self) -> str:
        return "white"
