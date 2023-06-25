from enum import Enum, auto

from analysis_code.constants.types import ConditionType


# reference to the rule type src.analysis_code.constants.rule_type
class NodeType(Enum):
    UNKNOWN = auto()  # Unknown node type
    IGNORE = auto()  # Node to be ignored
    STATEMENT = auto()  # Statement node
    DEF = auto()  # Function definition node
    CONDITIONS = auto()  # Conditional statement node
    LOOP = auto()  # Loop statement node
    RETURN = auto()  # Return statement node
    COMMENT = auto()  # Comment node
    EXPRESSION = auto()  # Expression node
    RAISE = auto()  # Raise statement node

    START = 1001
    END = 1002

    @classmethod
    def is_start(cls, node):
        return node.type == NodeType.START

    @classmethod
    def is_end(cls, node):
        return node.type == NodeType.END

    @classmethod
    def is_condition(cls, node):
        return node.type == NodeType.CONDITIONS

    @classmethod
    def is_statement(cls, node):
        return node.type == NodeType.STATEMENT

    @classmethod
    def is_return(cls, node):
        return node.type.name == NodeType.RETURN.name

    @classmethod
    def is_loop(cls, node):
        return node.type == NodeType.LOOP

    @classmethod
    def is_definition(cls, node):
        return node.type == NodeType.DEF

    @classmethod
    def is_raise(cls, node):
        return node.type == NodeType.RAISE

    @classmethod
    def is_comment(cls, node):
        return node.type == NodeType.COMMENT

    @classmethod
    def is_ignore(cls, node):
        return node.type == NodeType.IGNORE

    @classmethod
    def is_unknown(cls, node):
        return node.type == NodeType.UNKNOWN

    @classmethod
    def is_condition_elif(cls, node):
        return (
            node.type == NodeType.CONDITIONS
            and node.info_type == ConditionType.ELIF.name
        )
