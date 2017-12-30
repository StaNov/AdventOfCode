from adventofcode.problems.utils import InputFileParser as BaseParser
from .parsedinput import ParsedInput, Instruction


class InputFileParser(BaseParser):
    def parse(self, input_string):
        parsed_input = ParsedInput()

        lines = input_string.splitlines()

        for line in lines:
            (
                register_name,
                instruction_type,
                value_to_apply,
                __,  # "if"
                condition_register,
                condition_type,
                condition_value
            ) = line.split()

            parsed_input.add_instruction(
                register_name,
                parse_instruction_type(instruction_type),
                int(value_to_apply),
                condition_register,
                parse_condition_type(condition_type),
                int(condition_value)
            )

        return parsed_input


def parse_instruction_type(string):
    string_to_type = {
        "inc": Instruction.Type.INC,
        "dec": Instruction.Type.DEC
    }
    return string_to_type[string]


def parse_condition_type(string):
    string_to_type = {
        ">": Instruction.ConditionType.GREATER,
        ">=": Instruction.ConditionType.GREATER_EQUALS,
        "<": Instruction.ConditionType.LESSER,
        "<=": Instruction.ConditionType.LESSER_EQUALS,
        "==": Instruction.ConditionType.EQUALS,
        "!=": Instruction.ConditionType.NOT_EQUALS,
    }
    return string_to_type[string]
