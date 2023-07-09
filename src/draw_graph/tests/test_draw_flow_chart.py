import os
from unittest import TestCase

from constants import SRC_DIR

from src.draw_graph.services.dotfile_creator import DotfileCreator
from src.utils.file_handler import write_file


class TestDrawFlowChartWithAST(TestCase):
    current_dir = os.path.abspath(os.path.dirname(__file__))  # src/draw_graph/tests
    input_json_dir = os.path.join(
        SRC_DIR, "analysis_code/tests/data/output/json"
    )  # src/analysis_code/tests/data/output/json
    output_dir = os.path.join(
        current_dir, "data/output"
    )  # src/draw_graph/tests/data/output
    output_dot_dir = os.path.join(
        output_dir, "dot"
    )  # src/draw_graph/tests/data/output/dot
    output_svg_dir = os.path.join(
        output_dir, "svg"
    )  # src/draw_graph/tests/data/output/svg
    expected_dot_dir = os.path.join(
        current_dir, "data/expected"
    )  # src/draw_graph/tests/data/expected

    def test_draw_graph(self):
        input_files = os.listdir(self.input_json_dir)
        for input_file in input_files:
            self.__draw_graph(origin_file_name=input_file)
            # self.__compare_dot_files(origin_file_name=input_file)

    def __draw_graph(self, origin_file_name: str):
        input_json_full_path = os.path.join(self.input_json_dir, origin_file_name)
        output_dot_full_path = os.path.join(
            self.output_dot_dir, f"{origin_file_name}.dot"
        )
        output_svg_full_path = os.path.join(
            self.output_svg_dir, f"{origin_file_name}.svg"
        )

        dot_file_creator = DotfileCreator(file_path=input_json_full_path)
        content = dot_file_creator.generate()
        # write dot file
        write_file(output_dot_full_path, content)
        # convert dot to svg file
        os.system(f"dot -Tsvg {output_dot_full_path} -o {output_svg_full_path}")

    def __compare_dot_files(self, origin_file_name: str):
        actual_dot_full_path = os.path.join(
            self.output_dot_dir, f"{origin_file_name}.dot"
        )
        expected_dot_full_path = os.path.join(
            self.expected_dot_dir, f"{origin_file_name}.dot"
        )

        if not os.path.exists(expected_dot_full_path):
            return self.fail(
                f"Expected dot file {expected_dot_full_path} does not exist."
            )

        with open(actual_dot_full_path, "r") as actual_dot_file:
            actual_dot_content = actual_dot_file.read()
        with open(expected_dot_full_path, "r") as expected_dot_file:
            expected_dot_content = expected_dot_file.read()
        actual_dot_content = actual_dot_content.replace(" ", "").replace("\n", "")
        expected_dot_content = expected_dot_content.replace(" ", "").replace("\n", "")
        self.assertEqual(actual_dot_content, expected_dot_content)
