from ast import literal_eval
from dataclasses import dataclass, field
from typing import Any, Dict

from src.analysis_code.constants.types import ASTNodeType


@dataclass(repr=True)
class ACNode:
    _info: Dict[str, Any] = field(default_factory=dict)
    _type: ASTNodeType = ASTNodeType.UNKNOWN
    _indent: int = 0
    _line_no: int = 0

    @property
    def info(self) -> Dict[str, Any]:
        return self._info

    @property
    def info_type(self) -> str:
        return self.info.get("type")

    @property
    def type(self) -> ASTNodeType:
        return self._type

    @property
    def line_no(self) -> int:
        return self._line_no

    @property
    def indent(self) -> int:
        return self._indent

    @classmethod
    def from_string(cls, string: str) -> "ACNode":
        data: Dict[str, Any] = literal_eval(string)
        return cls.from_dict(data)

    @classmethod
    def from_dict(cls, data: Dict[str, Any] = field(default_factory=dict)) -> "ACNode":
        _info = data.get("info", {})
        _type = data.get("type", ASTNodeType.UNKNOWN)
        _indent = data.get("indent", 0)
        _line_no = data.get("line_no", 0)
        return cls(_info=_info, _type=_type, _indent=_indent, _line_no=_line_no)

    def to_dict(self) -> Dict[str, Any]:
        return dict(
            info=self._info, type=self._type, indent=self._indent, line_no=self._line_no
        )
