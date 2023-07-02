from typing import TYPE_CHECKING

from src.draw_graph.constants.node_types import NodeType

if TYPE_CHECKING:
    from src.draw_graph.models.dg_node import DGNode


class SimpleNodeConnection:
    def __init__(
        self,
        start: str,
        end: str,
        label: str = "",
        source: str = "",
        color: str = "",
        fontcolor: str = "",
    ):
        self._start = start
        self._end = end
        self._label = label
        self._source = source
        self._color = color
        self._fontcolor = fontcolor

    @property
    def is_valid(self) -> bool:
        return self._start and self._end

    def to_dot(self) -> str:
        if not self.is_valid:
            return ""

        fields = [
            self.build_color(),
            self.build_fontcolor(),
            self.build_label(self._label),
            self.build_source(self._source),
        ]
        return f"{self._start} -> {self._end} {' '.join(fields)}"

    def build_color(self) -> str:
        return f"[color={self._color}]" if self._color else ""

    def build_fontcolor(self) -> str:
        return f"[fontcolor={self._fontcolor}]" if self._fontcolor else ""

    def build_label(self, label: str) -> str:
        return f"[label={self._label}]" if label else ""

    def build_source(self, source: str) -> str:
        debug_data = f"{source}".replace('"', "'")
        return f'[source="{debug_data}"]' if debug_data else ""

    def __repr__(self):
        return f"{self._start} -> {self._end} with label {self._label}"


class NodeConnection(SimpleNodeConnection):
    def __init__(
        self,
        start_node: "DGNode",
        end_node: "DGNode",
        label: str = "",
        source: str = "",
        color: str = "",
        fontcolor: str = "",
    ):
        self._start_node = start_node
        self._end_node = end_node
        super().__init__(
            start_node.id,
            end_node.id,
            label=label,
            source=source,
            color=color,
            fontcolor=fontcolor,
        )

    def to_dot(self) -> str:
        if any(
            [not self.is_valid, self._start_node.is_hidden, self._end_node.is_hidden]
        ):
            return ""
        return super().to_dot()

    @property
    def is_valid(self):
        return self._start_node and self._end_node and not self.is_invalid()

    def is_invalid(self) -> bool:
        return any([self.is_invalid_start_return()])

    def is_invalid_start_return(self) -> bool:
        return NodeType.is_return(self._start_node) and not NodeType.is_end(
            self._end_node
        )
