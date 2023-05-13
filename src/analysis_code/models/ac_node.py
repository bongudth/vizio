import json
from ast import literal_eval
from typing import Any, Dict, Optional

from src.analysis_code.constants.types import ASTNodeType


def parse_line(line):
    return json.loads(line)


class ACNode:
    def __init__(
        self, info: Optional[Dict] = None, type: Optional[ASTNodeType] = None, indent=0
    ):
        self._info = info or {}
        self._type = ASTNodeType(type) if type else None
        self._indent = indent

    @property
    def type(self) -> ASTNodeType:
        return self._type

    @property
    def info_type(self):
        return self.info.get("type")

    @property
    def info(self) -> Dict[str, Any]:
        return self._info

    @property
    def indent(self) -> int:
        return self._indent

    def from_string(self, string: str):
        data = literal_eval(string)
        self.from_dict(data)
        return self

    def from_dict(self, data=None):
        self._type = data.get("type")
        self._info = data.get("info")
        self._indent = data.get("indent", 0)
        return self

    def to_dict(self):
        return dict(type=self._type, info=self._info, indent=self._indent)

    def __repr__(self):
        return f"ACNode(info={self.info}, type={self.type}, indent={self.indent})"
