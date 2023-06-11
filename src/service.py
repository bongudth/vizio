from src.analysis_code.services.code_reader import CoderReader
from src.draw_graph.services.dotfile_creator import DotfileCreator


def generate_dot(source_code: str):
    if not source_code:
        raise ValueError("source_code is required!")

    code_reader = CoderReader()
    results = code_reader.parse_string(source_code)

    dot_file_creator = DotfileCreator(results)
    content = dot_file_creator.generate()

    return content
