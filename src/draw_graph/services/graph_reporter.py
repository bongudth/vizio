class GraphReporter:
    def __init__(self):
        self.nodes = []
        self.connections = []

    def get_report(self, node_structure):
        self.nodes = node_structure.get_dg_nodes()
        self.connections = node_structure.get_node_connections()
        return dict(n_nodes=len(self.nodes), n_connections=len(self.connections))
