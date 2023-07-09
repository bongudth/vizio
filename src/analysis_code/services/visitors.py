import ast
from _ast import AST, Assert, AugAssign, Call, Continue, Expr, For, FunctionDef, Return
from typing import Any, Dict, List

from src.analysis_code.constants.types import (
    ASTNodeType,
    ConditionType,
    LoopType,
    StatementType,
)
from src.analysis_code.models.ac_node import ACNode


class PythonVisitor(ast.NodeVisitor):
    def __init__(self):
        self.data_stack: List[Dict] = []
        self.output: List[ACNode] = []

    def visit_If(self, node):
        type = ASTNodeType.CONDITIONS
        value = ast.unparse(node.test)
        condition_type = ConditionType.IF
        info_data = {"type": condition_type.name, "value": value, "conditions": value}
        if self._is_else(node):
            condition_type = ConditionType.ELSE
            else_info_data = {
                "type": condition_type.name,
            }
            else_data = {
                id(node.orelse[0]): {"node": node, "type": type, "info": else_info_data}
            }
            self.data_stack.append(else_data)

        elif self._is_elif(node):
            condition_type = ConditionType.ELIF
            info_data["type"] = condition_type.name

        self.custom_visit(node, type, info=info_data)

    def visit_Assign(self, node):
        type = ASTNodeType.STATEMENT
        value = ast.unparse(node)
        info_data = {
            "value": value,
            "info": {
                "type": StatementType.ASSIGN.name,
            },
        }
        return self.custom_visit(node, type, info=info_data)

    def visit_AnnAssign(self, node):
        type = ASTNodeType.STATEMENT
        value = ast.unparse(node)
        info_data = {
            "value": value,
            "info": {
                "type": StatementType.ASSIGN.name,
            },
        }
        return self.custom_visit(node, type, info=info_data)

    def visit_Return(self, node: Return) -> Any:
        type = ASTNodeType.RETURN
        if not node.value:
            return self.custom_visit(node, type)

        value = ast.unparse(node.value)
        info_data = {
            "value": value,
            "name": value,
        }
        return self.custom_visit(node, type, info=info_data)

    def visit_Call(self, node: Call) -> Any:
        type = ASTNodeType.STATEMENT
        value = ast.unparse(node)
        info_data = {
            "value": value,
            "type": StatementType.METHOD.name,
        }
        return self.custom_visit(node, type, info=info_data)

    def visit_Expr(self, node: Expr) -> Any:
        type = ASTNodeType.STATEMENT
        value = ast.unparse(node)
        info_data = {
            "value": value,
            "type": StatementType.METHOD.name,
        }
        return self.custom_visit(node, type, info=info_data)

    def visit_FunctionDef(self, node: FunctionDef) -> Any:
        type = ASTNodeType.DEF
        name = node.name
        value = ast.unparse(node).split("\n")[0].replace(":", "")
        info_data = {"value": value, "name": name, "args": ast.unparse(node.args)}
        return self.custom_visit(node, type, info=info_data)

    def visit_For(self, node: For) -> Any:
        type = ASTNodeType.LOOP
        info_data = {
            "type": LoopType.FOR.name,
            "item": ast.unparse(node.target),
            "list": ast.unparse(node.iter),
        }
        return self.custom_visit(node, type, info=info_data)

    def visit_While(self, node: ast.While) -> Any:
        type = ASTNodeType.LOOP
        info_data = {
            "type": LoopType.WHILE.name,
            "conditions": ast.unparse(node.test),
        }
        return self.custom_visit(node, type, info=info_data)

    def visit_Raise(self, node: ast.Raise) -> Any:
        type = ASTNodeType.RAISE
        info_data = {
            "type": type.name,
            "value": ast.unparse(node.exc),
        }
        return self.custom_visit(node, type, info=info_data)

    def visit_AugAssign(self, node: AugAssign) -> Any:
        type = ASTNodeType.STATEMENT
        value = ast.unparse(node)
        info_data = {
            "value": value,
            "type": StatementType.ASSIGN.name,
        }
        return self.custom_visit(node, type, info=info_data)

    def visit_Continue(self, node: Continue) -> Any:
        type = ASTNodeType.STATEMENT
        info_data = {
            "type": StatementType.CONTINUE.name,
        }
        return self.custom_visit(node, type, info=info_data)

    def visit_Break(self, node: Continue) -> Any:
        type = ASTNodeType.STATEMENT
        info_data = {
            "type": StatementType.BREAK.name,
        }
        return self.custom_visit(node, type, info=info_data)

    def visit_Assert(self, node: Assert) -> Any:
        type = ASTNodeType.STATEMENT
        value = ast.unparse(node)
        info_data = {
            "value": value,
            "type": StatementType.ASSERT.name,
        }
        return self.custom_visit(node, type, info=info_data)

    def custom_visit(self, node: AST, type=ASTNodeType.UNKNOWN, **kwargs) -> Any:
        last_line_no = self.output[-1].line_no if self.output else 0
        if node.lineno == last_line_no:
            return

        if self.data_stack and id(node) in self.data_stack[-1]:
            stack_node = self.data_stack.pop()
            data = stack_node[id(node)]
            self._append_acnode(**data)

        self._append_acnode(node, type=type, **kwargs)
        return self.generic_visit(node)

    def _append_acnode(self, node, type, **kwargs) -> None:
        data = {
            "type": type.name,
            "info": {},
            "indent": node.col_offset,
            "line_no": node.lineno,
        }
        if info_data := kwargs.get("info"):
            data["info"].update(info_data)

        ac_node = ACNode().from_dict(data)
        self.output.append(ac_node)

    def _is_else(self, node: AST) -> bool:
        return (
            node.orelse
            and len(node.orelse) > 0
            and not isinstance(node.orelse[0], ast.If)
        )

    def _is_elif(self, node: AST) -> bool:
        return (
            hasattr(node, "parent")
            and hasattr(node.parent, "orelse")
            and node.parent.orelse
        )
