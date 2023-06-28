import os
from unittest import TestCase

from constants import SRC_DIR

from src.draw_graph.services.dotfile_creator import DotfileCreator
from src.utils.file_handler import write_file


class TestDrawFlowChartWithAST(TestCase):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    test_dir = os.path.abspath(os.path.dirname(current_dir))
    test_data_dir = os.path.join(SRC_DIR, "analysis_code/tests/data/output")
    dotfiles_path = "data/dotfiles"
    dotfiles_dir = os.path.join(current_dir, dotfiles_path)

    def test_draw_fibo(self):
        self.__write_dotfile(origin_file_name="fibo.py.json")

    def test_draw_if_else(self):
        self.__write_dotfile(origin_file_name="if_else.py.json")

    def test_draw_insertion_sort(self):
        self.__write_dotfile(origin_file_name="insertion_sort.py.json")

    def test_draw_node_connections(self):
        self.__write_dotfile(origin_file_name="node_connections.py.json")

    def test_draw_bucket_sort(self):
        self.__write_dotfile(origin_file_name="bucket_sort.py.json")

    def test_draw_counting_sort(self):
        self.__write_dotfile(origin_file_name="counting_sort.py.json")

    def test_draw_intersection(self):
        self.__write_dotfile(origin_file_name="intersection.py.json")

    def test_draw_lower_upper_decomposition(self):
        self.__write_dotfile(origin_file_name="lower_upper_decomposition.py.json")

    def test_draw_quick_sort(self):
        self.__write_dotfile(origin_file_name="quick_sort.py.json")

    def test_draw_find_max(self):
        self.__write_dotfile(origin_file_name="find_max.py.json")

    def test_draw_secant_method(self):
        self.__write_dotfile(origin_file_name="secant_method.py.json")

    def test_draw_shell_sort(self):
        self.__write_dotfile(origin_file_name="shell_sort.py.json")

    def __write_dotfile(self, origin_file_name: str):
        ast_path = os.path.join(self.test_data_dir, origin_file_name)
        dot_full_path = os.path.join(self.dotfiles_dir, f"{origin_file_name}.dot")

        dot_file_creator = DotfileCreator(file_path=ast_path)
        content = dot_file_creator.generate()
        # write dot file
        write_file(dot_full_path, content)
        # convert dot to svg file
        svg_full_path = dot_full_path.replace(".dot", ".svg")
        os.system(f"dot -Tsvg {dot_full_path} -o {svg_full_path}")
