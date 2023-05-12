from src.draw_graph.models.dg_node import DGNode


class BaseConnectionHandler:
    _text = None
    _connections = None

    def __init__(self, node: "DGNode"):
        self.node = node
        self._text = ""
        self._connections = []

    @property
    def text(self):
        return self._text

    @property
    def connections(self):
        return self._connections

    def handle(self):
        raise NotImplementedError

    @property
    def color(self) -> str:
        return ""
