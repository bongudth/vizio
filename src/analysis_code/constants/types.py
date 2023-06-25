from enum import Enum, auto


class ASTNodeType(Enum):
    """
    Enumeration representing the different types of nodes in an abstract syntax tree.
    """

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


class ConditionType(Enum):
    """
    Enumeration representing the different types of conditions in an abstract syntax tree.
    """

    IF = auto()
    ELIF = auto()
    ELSE = auto()


class StatementType(Enum):
    """
    Enumeration representing the different types of statements in an abstract syntax tree.
    """

    ASSIGN = auto()
    METHOD = auto()
    RAISE = auto()


class LoopType(Enum):
    """
    Enumeration representing the different types of loops in an abstract syntax tree.
    """

    FOR = auto()
    WHILE = auto()
    UNKNOWN = auto()
