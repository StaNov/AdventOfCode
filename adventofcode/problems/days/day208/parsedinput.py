from enum import Enum


class ParsedInput:
    def __init__(self, register_name):
        self.instructions = [Instruction(register_name)]


class Instruction:
    def __init__(self, register_name):
        self.register_name = register_name
        self.type = Instruction.Type.INC

    class Type(Enum):
        INC = 0
