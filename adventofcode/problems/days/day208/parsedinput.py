from enum import Enum


class ParsedInput:
    def __init__(self, register_name, instruction_type):
        self.instructions = [Instruction(register_name, instruction_type)]


class Instruction:
    def __init__(self, register_name, instruction_type):
        self.register_name = register_name
        self.type = instruction_type

    class Type(Enum):
        INC = 0
        DEC = 1
