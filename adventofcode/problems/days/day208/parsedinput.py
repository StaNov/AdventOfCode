from enum import Enum


class ParsedInput:
    def __init__(self, register_name, instruction_type, value_to_apply):
        self.instructions = [Instruction(register_name, instruction_type, value_to_apply)]


class Instruction:
    def __init__(self, register_name, instruction_type, value_to_apply):
        self.register_name = register_name
        self.type = instruction_type
        self.value_to_apply = value_to_apply

    class Type(Enum):
        INC = 0
        DEC = 1
