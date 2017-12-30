from enum import Enum


class ParsedInput:
    def __init__(self, register_name, instruction_type, value_to_apply, condition_register):
        self.instructions = [Instruction(register_name, instruction_type, value_to_apply, condition_register)]


class Instruction:
    def __init__(self, register_name, instruction_type, value_to_apply, condition_register):
        self.register_name = register_name
        self.type = instruction_type
        self.value_to_apply = value_to_apply
        self.condition_register = condition_register

    class Type(Enum):
        INC = 0
        DEC = 1
