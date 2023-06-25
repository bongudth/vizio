import json
from typing import List

from src.draw_graph.services.dotfile_creator.dotfile_body_creator import (
    DotfileBodyCreator,
)
from src.draw_graph.services.dotfile_creator.dotfile_header_creator import (
    DotfileHeaderCreator,
)
from src.utils.file_handler import read_file


class DotfileCreator:
    def __init__(self, **kwargs):
        self._file_path = kwargs.get("file_path")
        self._lines = kwargs.get("lines")
        self._content = ""

        if self._file_path:
            if self._file_path.endswith(".json"):
                self._lines = self._read_json()
            elif self._file_path.endswith(".txt"):
                self._lines = self._read_txt()
            else:
                raise Exception("Invalid file path")

    def generate(self) -> str:
        return self._create_dotfile()

    def _read_json(self) -> List[dict]:
        with open(self._file_path, "r") as f:
            return json.load(f)

    def _read_txt(self) -> List[dict]:
        return read_file(self._file_path)

    def _create_dotfile(self):
        self._content = DotfileHeaderCreator("my_graph").wrap(
            DotfileBodyCreator(self._lines).create()
        )
        return self._content

    @property
    def content(self):
        return self._content
