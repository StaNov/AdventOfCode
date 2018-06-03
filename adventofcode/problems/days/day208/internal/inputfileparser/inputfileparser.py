from adventofcode.problems.framework import InputFileParser as BaseParser
from adventofcode.problems.days.day208.internal.instruction import InstructionType, InstructionConditionType
from adventofcode.problems.days.day208.internal.inputfileparser.parsedinput import ParsedInput


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
                _parse_instruction_type(instruction_type),
                int(value_to_apply),
                condition_register,
                _parse_condition_type(condition_type),
                int(condition_value)
            )

        return parsed_input


def _parse_instruction_type(string):
    string_to_type = {
        "inc": InstructionType.INC,
        "dec": InstructionType.DEC
    }
    return string_to_type[string]


def _parse_condition_type(string):
    string_to_type = {
        ">": InstructionConditionType.GREATER,
        ">=": InstructionConditionType.GREATER_EQUALS,
        "<": InstructionConditionType.LESSER,
        "<=": InstructionConditionType.LESSER_EQUALS,
        "==": InstructionConditionType.EQUALS,
        "!=": InstructionConditionType.NOT_EQUALS,
    }
    return string_to_type[string]
