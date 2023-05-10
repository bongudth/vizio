from enum import Enum


class ASTNodeType(Enum):
    UNKNOWN = 0
    IGNORE = 1
    DEF = 2
    CONDITIONS = 3
    RETURN = 4
    LOOP = 5
    COMMENT = 6
    STATEMENT = 7

    def __str__(self):
        return self.name


class ConditionType(Enum):
    IF = 1
    ELIF = 2
    ELSE = 3

    def __str__(self):
        return self.name


class StatementType(Enum):
    STATEMENT_ASSIGN = 1
    STATEMENT_METHOD = 2
