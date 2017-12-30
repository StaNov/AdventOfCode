from adventofcode.problems.utils import InputFileParser as BaseParser
from .parsedinput import ParsedInput, Instruction


class InputFileParser(BaseParser):
    def parse(self, input_string):
        (
            register_name,
            instruction_type,
            value_to_apply,
            __,  # "if"
            condition_register,
            condition_type,
            __
        ) = input_string.split()

        return ParsedInput(
            register_name,
            parse_instruction_type(instruction_type),
            int(value_to_apply),
            condition_register,
            parse_condition_type(condition_type)
        )


def parse_instruction_type(string):
    string_to_type = {
        "inc": Instruction.Type.INC,
        "dec": Instruction.Type.DEC
    }
    return string_to_type[string]


def parse_condition_type(string):
    string_to_type = {
        ">": Instruction.ConditionType.GREATER,
        ">=": Instruction.ConditionType.GREATER_EQUALS
    }
    return string_to_type[string]
