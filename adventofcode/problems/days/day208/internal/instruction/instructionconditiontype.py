from enum import Enum


class InstructionConditionType(Enum):
    GREATER = 0
    GREATER_EQUALS = 1
    LESSER = 2
    LESSER_EQUALS = 3
    EQUALS = 4
    NOT_EQUALS = 5
