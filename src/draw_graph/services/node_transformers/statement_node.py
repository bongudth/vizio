from src.analysis_code.constants.types import StatementType
from src.draw_graph.constants.shape import ShapeType
from src.draw_graph.services.node_transformers.base_dot_node import NodeTransformerBase


class StatementNode(NodeTransformerBase):
    """
    Transform a conditional node to dotfile format
    """

    @property
    def label(self) -> str:
        return self.node.info.get("value")

    @property
    def shape(self):
        statement_type = StatementType[self.node.info.get("type")]
        if statement_type == StatementType.STATEMENT_METHOD:
            return ShapeType.PARALLELOGRAM.value
        return ShapeType.RECTANGLE.value

    @property
    def color(self):
        return ""

    @property
    def fill_color(self) -> str:
        return "#FFC6D3"

    @property
    def font_color(self) -> str:
        return "black"
