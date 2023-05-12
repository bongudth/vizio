from src.draw_graph.services.node_transformers.base_dot_node import NodeTransformerBase


class DefinitionNode(NodeTransformerBase):
    """
    Transform a conditional node to dotfile format
    """

    @property
    def label(self):
        return ""

    @property
    def shape(self):
        return ""

    @property
    def color(self):
        return ""
