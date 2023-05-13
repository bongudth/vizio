from typing import List


def write_file(filename, content):
    """
    It opens a file, writes some content to it, and then closes the file.

    :param filename: The name of the file to write to
    :param content: The content of the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)


def read_file(file_path) -> List[str]:
    """
    It reads the file at the given path and returns a list of strings, each string being a line from the
    file
    :param file_path: The path to the file you want to read
    :return: A list of strings.
    """
    lines = []
    with open(file_path, encoding="utf-8") as f:
        lines = f.readlines()
    return lines
