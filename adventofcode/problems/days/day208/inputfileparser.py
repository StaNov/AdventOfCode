from adventofcode.problems.utils import InputFileParser as BaseParser
from .parsedinput import ParsedInput


class InputFileParser(BaseParser):
    def parse(self, input_string):
        register_name, instruction_type, __, __, __, __, __ = input_string.split()
        return ParsedInput(register_name)
