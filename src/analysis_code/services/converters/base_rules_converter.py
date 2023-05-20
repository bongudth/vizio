from abc import ABC


class BaseRulesConverter(ABC):
    KEYWORDS = []
    DEBUG = False
    AST_NODE_TYPE = None

    @classmethod
    def can_handle(cls, sentence: str):
        if not cls.KEYWORDS:
            return True

        can_handle = any(
            sentence.strip().startswith(keyword) for keyword in cls.KEYWORDS
        )
        if cls.DEBUG:
            print(f"can_handle: {cls.__name__} - {can_handle}")
        return can_handle
