from src.analysis_code.constants.types import ConditionType
from src.draw_graph.constants.shape import ShapeType
from src.draw_graph.services.node_transformers.base_dot_node import NodeTransformerBase


class ConditionNode(NodeTransformerBase):
    """
    Transform a conditional node to dotfile format
    """

    @property
    def is_hidden(self) -> bool:
        return self.node.info_type == ConditionType.ELSE.name

    @property
    def label(self):
        conditions = self.node.info.get("conditions")
        return ", ".join(conditions) if conditions else str(self.node.info)

    @property
    def shape(self):
        return ShapeType.DIAMOND.value

    @property
    def color(self):
        return ""

    @property
    def fill_color(self) -> str:
        return "#ECB365"

    @property
    def font_color(self) -> str:
        return "black"
