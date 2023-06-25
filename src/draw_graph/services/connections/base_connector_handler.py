from src.draw_graph.models.dg_node import DGNode


class BaseConnectionHandler:
    _text = None
    _connections = None

    def __init__(self, node: "DGNode", **kwargs):
        self.node = node
        self._text = ""
        self._connections = []

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def connections(self):
        return self._connections

    @connections.setter
    def connections(self, value):
        self._connections = value

    def handle(self, **kwargs) -> tuple:
        return self.handle_connections(**kwargs)

    def handle_connections(self, **kwargs) -> tuple:
        raise NotImplementedError

    @property
    def color(self) -> str:
        return ""

    @property
    def is_hidden(self) -> bool:
        return self.node.is_hidden
