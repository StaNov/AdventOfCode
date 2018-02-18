from enum import Enum


class InstructionType(Enum):
    INC = 0
    DEC = 1


class InstructionConditionType(Enum):
    GREATER = 0
    GREATER_EQUALS = 1
    LESSER = 2
    LESSER_EQUALS = 3
    EQUALS = 4
    NOT_EQUALS = 5


class Instruction:
    def __init__(self,
                 register_name,
                 instruction_type,
                 value_to_apply):
        self.register_name = register_name
        self.type = instruction_type
        self.value_to_apply = value_to_apply


class InstructionWithCondition(Instruction):
    def __init__(self,
                 register_name,
                 instruction_type,
                 value_to_apply,
                 condition_register,
                 condition_type,
                 condition_value):
        super().__init__(register_name, instruction_type, value_to_apply)
        self.condition_register = condition_register
        self.condition_type = condition_type
        self.condition_value = condition_value
