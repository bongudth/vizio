import json

from src.analysis_code.services.code_reader import CoderReader
from src.draw_graph.services.dotfile_creator import DotfileCreator
from src.summary_code import you_summary_code
from src.utils.file_handler import write_file


def generate_dot(source_code: str):
    if not source_code:
        raise ValueError("source_code is required!")

    code_reader = CoderReader()
    results = code_reader.parse_string(lines=source_code)

    dot_file_creator = DotfileCreator(results)
    content = dot_file_creator.generate()

    return content


def generate_dot_v2(source_code: str, need_summary=False):
    if not source_code:
        raise ValueError("source_code is required!")

    code_reader = CoderReader()
    results = code_reader.parse_string_from_ast(source_code)

    if need_summary:
        response = you_summary_code(results)
        list_summary = json.loads(response)

    dot_file_creator = DotfileCreator(lines=results, list_summary=list_summary)
    content = dot_file_creator.generate()
    return content
