from typing import List

from src.draw_graph.services.dotfile_creator.dotfile_body_creator import (
    DotfileBodyCreator,
)
from src.draw_graph.services.dotfile_creator.dotfile_header_creator import (
    DotfileHeaderCreator,
)


class DotfileCreator:
    def __init__(self, lines: List[str]):
        self._lines = lines
        self._content = DotfileHeaderCreator("my_graph").wrap(
            DotfileBodyCreator(lines).create()
        )

    def generate(self):
        return self._content
