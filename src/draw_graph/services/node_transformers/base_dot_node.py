from typing import TYPE_CHECKING, Any, Dict, Union

from src.analysis_code.models.ac_node import ACNode

if TYPE_CHECKING:
    from src.draw_graph.models.dg_node import DGNode


class NodeTransformerBase:
    """
    Transform a dg_node to dotfile format
    """

    def __init__(self):
        self.node: Union[ACNode, None] = None
        self.content = ""

    def transform(self, node: "DGNode") -> str:
        self.node = node
        params = self.get_params()
        if params.get("is_hidden"):
            return ""
        rendered_params: dict = params.get("render")
        return " ".join(str(s) for s in rendered_params.values() if s)

    def get_params(self) -> Dict[str, Any]:
        params = {"is_hidden": self.is_hidden}
        render_params = self._get_render_params()
        params["render"] = render_params
        return params

    def _get_render_params(self) -> Dict[str, Any]:
        self.node_id = self.node.id
        render_params = {"id": f"{self.node_id}"}
        if self.shape:
            render_params["shape"] = f"[shape={self.shape}]"
        if self.color:
            render_params["color"] = f"[color={self.color}]"
        if self.label:
            render_params["label"] = f'[label="{self._format_label(self.label)}"]'
            render_params["type"] = f'[type="{self.node.type.name}"]'
        if self.fill_color:
            render_params[
                "fill_color"
            ] = f'[style=filled fillcolor="{self.fill_color}" fontcolor={self.font_color}]'
        return render_params

    @property
    def label(self) -> str:
        return ""

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
