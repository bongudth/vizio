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

    # def test_draw_fibo(self):
    #     self.__write_dotfile(origin_file_name="fibo.py.json")

    # def test_draw_if_else(self):
    #     self.__write_dotfile(origin_file_name="if_else.py.json")

    # def test_draw_insertion_sort(self):
    #     self.__write_dotfile(origin_file_name="insertion_sort.py.json")

    # def test_draw_node_connections(self):
    #     self.__write_dotfile(origin_file_name="node_connections.py.json")

    # def test_draw_bucket_sort(self):
    #     self.__write_dotfile(origin_file_name="bucket_sort.py.json")

    # def test_draw_counting_sort(self):
    #     self.__write_dotfile(origin_file_name="counting_sort.py.json")

    # def test_draw_intersection(self):
    #     self.__write_dotfile(origin_file_name="intersection.py.json")

    # def test_draw_lower_upper_decomposition(self):
    #     self.__write_dotfile(origin_file_name="lower_upper_decomposition.py.json")

    # def test_draw_quick_sort(self):
    #     self.__write_dotfile(origin_file_name="quick_sort.py.json")

    # def test_draw_find_max(self):
    #     self.__write_dotfile(origin_file_name="find_max.py.json")

    # def test_draw_secant_method(self):
    #     self.__write_dotfile(origin_file_name="secant_method.py.json")

    # def test_draw_shell_sort(self):
    #     self.__write_dotfile(origin_file_name="shell_sort.py.json")

    def test_draw_graph(self):
        input_files = os.listdir(self.input_json_dir)
        for input_file in input_files:
            self.__draw_graph(origin_file_name=input_file)

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
