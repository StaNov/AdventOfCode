from .parsedinput import ParsedInput
from adventofcode.problems.utils import InputFileParser as BaseParser


class InputFileParser(BaseParser):
    def parse(self, input_string):
        return ParsedInput()
