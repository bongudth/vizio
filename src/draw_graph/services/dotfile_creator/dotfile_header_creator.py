class DotfileHeaderCreator:
    def __init__(self, graph_name: str):
        self.graph_name = graph_name

    def wrap(self, body: str):
        return f"digraph {self.graph_name} {{\n{body}\n}}"

    def __repr__(self):
        return f"DotfileHeaderCreator(graph_name={self.graph_name})"
