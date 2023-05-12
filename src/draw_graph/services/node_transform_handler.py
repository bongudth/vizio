from typing import Any, Dict, Optional, Type

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


class NodeTransformerHandler:
    """
    Transform a ac node to dotfile format
    """

    def __init__(self):
        self.node = None
        self.ignored_transforms = [
            NodeType.COMMENT,
            NodeType.IGNORE,
        ]
        self.transformer: Optional[NodeTransformerBase] = None

    def transform(self, node: DGNode) -> Dict[str, Any]:
        if node.type in self.ignored_transforms:
            return {}
        self.node = node
        node_id = id(self.node)
        self.transformer = self.get_transformer(node)
        content = f"{self.transformer().transform(node)}\n"
        return {
            "node_id": node_id,
            "content": content,
        }

    @classmethod
    def get_transformer(cls, node: DGNode) -> Type[NodeTransformerBase]:
        node_type: NodeType = node.type
        transformer_map = {
            NodeType.CONDITIONS: ConditionNode,
            NodeType.STATEMENT: StatementNode,
            NodeType.RETURN: ReturnNode,
            NodeType.DEF: DefinitionNode,
            NodeType.START: StartNode,
            NodeType.LOOP: LoopNode,
            NodeType.END: EndNode,
            NodeType.COMMENT: CommentNode,
        }
        return transformer_map.get(node_type) or DefaultNode
