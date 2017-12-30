from adventofcode.problems.utils import InputFileParser as BaseParser
from .parsedinput import ParsedInput, Instruction


class InputFileParser(BaseParser):
    def parse(self, input_string):
        register_name, instruction_type, __, __, __, __, __ = input_string.split()
        return ParsedInput(
            register_name,
            string_to_instruction_type(instruction_type)
        )


def string_to_instruction_type(string):
    string_to_type = {
        "inc": Instruction.Type.INC,
        "dec": Instruction.Type.DEC
    }
    return string_to_type[string]
