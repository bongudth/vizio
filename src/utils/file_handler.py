from typing import List


def read_file(file_path: str) -> List[str]:
    """
    Read file and return list of lines
    :param file_path: path to file
    :return: list of lines
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def write_file(file_path: str, lines: List[str]) -> None:
    """
    Write lines to file
    :param file_path: path to file
    :param lines: list of lines
    """
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(lines)
