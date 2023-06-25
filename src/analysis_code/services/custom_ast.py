import ast
from typing import List

from analysis_code.models.ac_node import ACNode


class CustomAstService:
    def __init__(self, visitor: ast.NodeVisitor, source_code: str = None):
        self.output = []
        self.visitor = visitor
        if source_code:
            self.parse(source_code)

    def parse(self, source_code: str):
        tree = ast.parse(source_code)
        self._append_parent_nodes(tree)
        self.output = self._use_visitor(tree, self.visitor)
        return self.output

    def render(self):
        return ast.dump(self.output, indent=4)

    def _use_visitor(self, tree: ast.AST, visitor: ast.NodeVisitor) -> List[ACNode]:
        visitor.visit(tree)
        return visitor.output

    def _append_parent_nodes(self, node: ast.AST):
        for child in ast.iter_child_nodes(node):
            child.parent = node
