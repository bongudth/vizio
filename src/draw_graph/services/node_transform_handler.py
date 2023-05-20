from typing import Any, Dict, Type

from src.draw_graph.constants.node_types import NodeType
from src.draw_graph.models.dg_node import DGNode
from src.draw_graph.services.node_transformers.base_dot_node import NodeTransformerBase
from src.draw_graph.services.node_transformers.comment_node import CommentNode
from src.draw_graph.services.node_transformers.condition_node import ConditionNode
from src.draw_graph.services.node_transformers.default_node import DefaultNode
from src.draw_graph.services.node_transformers.definition_node import DefinitionNode
from src.draw_graph.services.node_transformers.end_node import EndNode
from src.draw_graph.services.node_transformers.loop_node import LoopNode
from src.draw_graph.services.node_transformers.return_node import ReturnNode
from src.draw_graph.services.node_transformers.start_node import StartNode
from src.draw_graph.services.node_transformers.statement_node import StatementNode

_TRANSFORMER_MAP = {
    NodeType.CONDITIONS: ConditionNode,
    NodeType.STATEMENT: StatementNode,
    NodeType.RETURN: ReturnNode,
    NodeType.DEF: DefinitionNode,
    NodeType.START: StartNode,
    NodeType.LOOP: LoopNode,
    NodeType.END: EndNode,
    NodeType.COMMENT: CommentNode,
}

_IGNORE_TRANSFORMS = {
    NodeType.COMMENT,
    NodeType.IGNORE,
    NodeType.UNKNOWN,
}


class NodeTransformerHandler:
    @classmethod
    def get_transformer(cls, node: DGNode) -> Type[NodeTransformerBase]:
        return _TRANSFORMER_MAP.get(node.type, DefaultNode)

    def transform(self, node: DGNode) -> Dict[str, Any]:
        print("transforming node", node)

        if not node or node.type in _IGNORE_TRANSFORMS:
            return {}

        transformer_class = self.get_transformer(node)
        transformer = transformer_class()
        content = f"{transformer.transform(node)}\n"
        return {
            "node_id": transformer.node_id,
            "content": content,
        }
