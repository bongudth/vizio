from typing import TYPE_CHECKING, Any, Dict, Union

from src.analysis_code.models.ac_node import ACNode

if TYPE_CHECKING:
    from src.draw_graph.models.dg_node import DgNode


class NodeTransformerBase:
    """
    Transform a dg_node to dotfile format
    """

    def __init__(self):
        self.node: Union[ACNode, None] = None
        self.content = ""

    def transform(self, node: "DgNode") -> str:
        self.node = node
        if self.params.get("is_hidden"):
            return ""
        rendered_params: dict = self.params.get("render")
        return " ".join([str(s) for s in list(rendered_params.values()) if s])

    @property
    def params(self) -> Dict[str, Any]:
        returned_value = {
            "is_hidden": self.is_hidden,
            "render": {
                "id": id(self.node),
                "shape": f"[shape={self.shape}]" if self.shape else None,
                "color": f"[color={self.color}]" if self.color else None,
                "label": f'[label="{self._format_label(self.label)}"]',
                "type": f'[type="{self.node.type.name}"]' if self.label else None,
                "fill_color": f'[style=filled fillcolor="{self.fill_color}" fontcolor={self.font_color}]'
                if self.fill_color
                else None,
            },
        }
        return {k: v for k, v in returned_value.items() if v is not None}

    @property
    def label(self) -> str:
        pass

    @property
    def shape(self) -> str:
        return ""

    @property
    def color(self) -> str:
        return ""

    @property
    def fill_color(self) -> str:
        return ""

    @property
    def font_color(self) -> str:
        return ""

    @property
    def is_hidden(self) -> bool:
        return False

    def _format_label(self, label):
        return label.replace('"', "'")
