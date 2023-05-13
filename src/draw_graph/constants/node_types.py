from enum import Enum


# reference to the rule type src.analysis_code.constants.rule_type
class NodeType(Enum):
    UNKNOWN = 0
    IGNORE = 1
    DEF = 2
    CONDITIONS = 3
    RETURN = 4
    LOOP = 5
    COMMENT = 6
    STATEMENT = 7

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
        return node.type == NodeType.RETURN

    @classmethod
    def is_loop(cls, node):
        return node.type == NodeType.LOOP

    @classmethod
    def is_definition(cls, node):
        return node.type == NodeType.DEF

    @classmethod
    def is_comment(cls, node):
        return node.type == NodeType.COMMENT

    @classmethod
    def is_ignore(cls, node):
        return node.type == NodeType.IGNORE

    @classmethod
    def is_unknown(cls, node):
        return node.type == NodeType.UNKNOWN
