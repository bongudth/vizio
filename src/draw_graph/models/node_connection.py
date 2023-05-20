from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.draw_graph.models.dg_node import DGNode


class NodeConnection:
    def __init__(
        self,
        start_node: "DGNode",
        end_node: "DGNode",
        label: str = "",
        source: str = "",
        color: str = "",
    ):
        self._start = start_node
        self._end = end_node
        self._label = label
        self._source = source
        self._color = color

    @property
    def is_valid(self):
        return self._start and self._end

    def to_dot(self) -> str:
        if self.__is_empty_dot():
            return ""
        fields = [
            self.build_color(),
            self.build_label(self._label),
            self.build_source(self._source),
        ]
        return f"{self._start.id} -> {self._end.id} {' '.join(fields)}"

    def build_color(self) -> str:
        return f"[color={self._color}]" if self._color else ""

    def build_label(self, label: str) -> str:
        return f"[label={self._label}]" if label else ""

    def build_source(self, source: str) -> str:
        debug_data = f"{source} : {self._start.data} -> {self._end.data}".replace(
            '"', "'"
        )
        return f'[source="{debug_data}"]' if debug_data else ""

    def __is_empty_dot(self) -> bool:
        return any([not self.is_valid, self._start.is_hidden, self._end.is_hidden])

    def __repr__(self):
        return f"{self._start} -> {self._end} with label {self._source}"
