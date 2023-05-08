import os

from src.utils.file_handler import read_file, write_file


class TestFileHandler:
    def test_file_handler(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(current_dir, "data/input/quick_sort.py")
        lines = read_file(file_path)
        des_path = os.path.join(current_dir, "data/output/quick_sort.py")
        write_file(des_path, lines)


if __name__ == "__main__":
    TestFileHandler().test_file_handler()
