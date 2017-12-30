from adventofcode.problems.utils import InputFileParser as BaseParser
from .parsedinput import ParsedInput


class InputFileParser(BaseParser):
    def parse(self, input_string):
        return ParsedInput(input_string.split()[0])
