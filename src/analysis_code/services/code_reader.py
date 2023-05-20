import traceback
from typing import Generator

from src.analysis_code.constants.types import ASTNodeType
from src.analysis_code.services.converters.comment_rules_converter import (
    CommentRulesConverter,
)
from src.analysis_code.services.converters.condition_rules_converter import (
    ConditionRulesConverter,
)
from src.analysis_code.services.converters.definition_rules_converter import (
    DefinitionRulesConverter,
)
from src.analysis_code.services.converters.import_rules_converter import (
    ImportRulesConverter,
)
from src.analysis_code.services.converters.loop_rules_converter import (
    LoopRulesConverter,
)
from src.analysis_code.services.converters.return_rules_converter import (
    ReturnRulesConverter,
)
from src.analysis_code.services.converters.statement_assign_rules_converter import (
    StatementAssignRulesConverter,
)
from src.analysis_code.services.converters.statement_method_rules_converter import (
    StatementMethodRulesConverter,
)
from src.logger.app_log import AppLog
from src.utils.file_handler import read_file


class CoderReader:
    converters = [
        ImportRulesConverter,
        DefinitionRulesConverter,
        ConditionRulesConverter,
        LoopRulesConverter,
        ReturnRulesConverter,
        CommentRulesConverter,
        StatementAssignRulesConverter,
        StatementMethodRulesConverter,
    ]

    def parse_file(self, file_path):
        return list(self.parse_lines(read_file(file_path)))

    def parse_string(self, source_code):
        return list(self.parse_lines(source_code.split("\n")))

    def parse_lines(self, lines) -> Generator[dict, None, None]:
        return (
            self.parse_line(line, line_no + 1)
            for line_no, line in enumerate(lines)
            if line.strip()
        )

    @classmethod
    def parse_line(cls, line: str, line_no: int) -> dict:
        response = {
            "type": ASTNodeType.UNKNOWN.name,
            "info": {},
            "indent": len(line) - len(line.lstrip(" ")),
            "line_no": line_no,
        }
        try:
            for converter in cls.converters:
                if not converter.can_handle(line):
                    continue

                result = converter.handle(line)
                if result:
                    response.update(
                        {
                            "type": converter.AST_NODE_TYPE.name,
                            "info": result,
                        }
                    )
                    break

        except Exception as e:
            AppLog.error(e)
            AppLog.error(traceback.format_exc())
        return response
